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

request_timeout = settings.REQUEST_TIME_OUT_GET_EMB

def client_request(host, port, in_tensor_name, in_tensor_dtype, img, model_spec_name):
    img = img.reshape(-1, img.shape[1], img.shape[0], 3)
    channel = implementations.insecure_channel(host, int(port))
    stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)
    request = predict_pb2.PredictRequest()
    request.model_spec.name = model_spec_name
    tensor_proto = tf.make_tensor_proto(img, dtype=in_tensor_dtype)
    request.inputs[in_tensor_name].CopyFrom(tensor_proto)
    predict_response = stub.Predict(request, timeout=request_timeout)
    return predict_response

def object_detect_img(img):
    img_h = img.shape[0]
    img_w = img.shape[1]
    img_resize = cv2.resize(img, (settings.YOLO_IMG_SIZE, settings.YOLO_IMG_SIZE))
    try:
        predict_response = client_request(host=settings.HOST_OBJ_DETECT, port=settings.PORT_OBJ_DETECT , in_tensor_name='images', 
            in_tensor_dtype=np.float32, img=img_resize, model_spec_name=settings.OBJ_DETECT_MODEL_NAME)
    except:
        return None
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
    return img

def get_emb(img, object_detect):
    emb = Embedding()
    if object_detect:
        img = object_detect_img(img)
    try:
        predict_response = client_request(host=settings.HOST_GET_EMB, port=settings.PORT_GET_EMB, in_tensor_name='images', in_tensor_dtype=np.float32,  img=img, model_spec_name=settings.GET_EMB_MODEL_NAME)
    except:
        return None
    json_response = json.loads(json_format.MessageToJson(predict_response))
    preds = json_response['outputs']['scores']['floatVal']
    embed = list(np.floor(np.multiply(preds, settings.QUANTITATION_FACTOR)))
    embed_str = emb.embed_to_str(embed)
    return embed_str

def convert_image(encoded_image):
    imgdata = base64.b64decode(encoded_image)
    nparr = np.fromstring(imgdata, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img
