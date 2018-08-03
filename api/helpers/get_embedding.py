from grpc.beta import implementations
import tensorflow as tf
import numpy as np
from tensorflow_serving.apis import prediction_service_pb2
from tensorflow_serving.apis import predict_pb2, classification_pb2, inference_pb2, regression_pb2
import cv2
from google.protobuf import json_format
import json
import time
from api.helpers.detect import decode_yolo
import base64 
from tabby_search import settings
from fashion.embedding import Embedding

host = '192.168.6.48'
port_obj_detect = 8001
port_get_emb = 9000

def get_emb(img, object_detect):
  emb = Embedding()
  if object_detect:
    img_h = img.shape[0]
    img_w = img.shape[1]
    img_resize = cv2.resize(img, (300, 300))
    img_resize = img_resize.reshape(-1, img_resize.shape[1], img_resize.shape[0], 3)

    channel = implementations.insecure_channel(host, int(port_obj_detect))
    stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

    data = {'in_tensor_name': 'images', 'in_tensor_dtype': np.float32, 'data': img_resize}

    request = predict_pb2.PredictRequest()
    request.model_spec.name = 'yolo'

    tensor_proto = tf.make_tensor_proto(data['data'], dtype=data['in_tensor_dtype'])

    request.inputs[data['in_tensor_name']].CopyFrom(tensor_proto)

    request_timeout = 10
    predict_response = stub.Predict(request, timeout=request_timeout)
    json_response = json.loads(json_format.MessageToJson(predict_response))
    score = np.array(json_response['outputs']['bounding_box']['floatVal'])
    boxes = decode_yolo(score.reshape(1, 9, 9 ,5, 8)[0], img_h, img_w)
    max_score = -1
    for box in boxes:
      if(box['score'] > max_score):
        x_max, y_max, x_min, y_min, label = box['xmax'], box['ymax'], box['xmin'], box['ymin'], box['label']
        max_score = box['score']
    if max_score > -1:
      img = img[y_min:y_max, x_min:x_max]
  
  img = img.reshape(-1, img.shape[1], img.shape[0], 3)

  channel = implementations.insecure_channel(host, int(port_get_emb))
  stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

  data = {'in_tensor_name': 'images', 'in_tensor_dtype': np.float32, 'data': img}

  request = predict_pb2.PredictRequest()
  request.model_spec.name = 'simple'

  tensor_proto = tf.make_tensor_proto(data['data'], dtype=data['in_tensor_dtype'])

  request.inputs[data['in_tensor_name']].CopyFrom(tensor_proto)
  request_timeout = 10

  predict_response = stub.Predict(request, timeout=request_timeout)
  json_response = json.loads(json_format.MessageToJson(predict_response))

  preds = json_response['outputs']['scores']['floatVal']

  embed = list(np.floor(np.multiply(preds, settings.QUANTITATION_FACTOR)))
  embed_str = emb.embed_to_str(embed)

  return embed_str

def convert_image(encoded_image):
  imgdata = base64.b64decode(encoded_image)
  nparr = np.fromstring(imgdata, np.uint8)
  img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  # print(img.shape)
  return img