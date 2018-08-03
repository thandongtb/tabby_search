# from django.core.management.base import BaseCommand
# import keras.backend as K
# import numpy as np
# import json
# from keras.models import model_from_json
# import tabby_search.settings as settings
# import redis
# import time
# from seller_images.helpers import base64_decode_image
# from fashion.embedding import Embedding
# import base64
# import uuid
# from io import BytesIO
# from PIL import Image
# from keras.applications.inception_v3 import preprocess_input
# from tabby_search.settings import IMAGE_WIDTH, IMAGE_HEIGHT
# from seller_images.helpers import base64_decode_image, base64_encode_image
# from keras.preprocessing import image as keras_image
# from yolo_object_detection.frontend import YOLO
# # from tabby_search.settings import YOLO_CONFIG_PATH, YOLO_MODEL_PATH
# import cv2

# config = K.tf.ConfigProto()
# config.gpu_options.allow_growth = True
# session = K.tf.Session(config=config)

# db = redis.StrictRedis(host=settings.REDIS_HOST,
#                        port=settings.REDIS_PORT, db=settings.REDIS_DB)

# class Command(BaseCommand):
#     help = 'Cached model deep learning for generate embedding'

#     def preprocess_image_worker(self, path):
#         img = Image.open((path)).convert('RGB')
#         img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))

#         x = keras_image.img_to_array(img)
#         x = np.expand_dims(x, axis=0)
#         x = preprocess_input(x)
#         return x

#     def get_encoded_image(self, base64_string):
#         image_decoded = BytesIO(base64.b64decode(base64_string))
#         image = self.preprocess_image_worker(image_decoded)
#         image = image.copy(order="C")

#         image = base64_encode_image(image)
#         return image

#     def load_deep_ranking_model(self):
#         # load json and create model
#         print("Loadding model...")
#         json_file = open(settings.MODEL_KERAS_JSON, 'r')
#         loaded_model_json = json_file.read()
#         json_file.close()
#         loaded_model = model_from_json(loaded_model_json)
#         # load weights into new model
#         loaded_model.load_weights(settings.MODEL_KERAS_WEIGHT)
#         print("Loaded model from disk")
#         return loaded_model

#     def load_yolo_model(self):
#         with open(YOLO_CONFIG_PATH) as config_buffer:
#             config = json.load(config_buffer)

#         model = YOLO(backend=config['model']['backend'],
#                     input_size=config['model']['input_size'],
#                     labels=config['model']['labels'],
#                     max_box_per_image=config['model']['max_box_per_image'],
#                     anchors=config['model']['anchors'])
#         model.load_weights(YOLO_MODEL_PATH)
#         return model

#     def base64_to_image(self, base64_string):
#         try:
#             imgdata = base64.b64decode(base64_string)
#             image = np.asarray(bytearray(imgdata), dtype="uint8")
#             image = cv2.imdecode(image, cv2.COLOR_BGR2RGB)
#             return image
#         except:
#             return np.array([])

#     def process_detected_image(self, base64_string):
#         encoded_image = self.get_encoded_image(base64_string)
#         image = base64_decode_image(encoded_image,
#                                     settings.IMAGE_DTYPE,
#                                     (1, settings.IMAGE_HEIGHT, settings.IMAGE_WIDTH,
#                                      settings.IMAGE_CHANS))
#         return image

#     def yolo_predict(self, base64_string, yolo_model):
#         try:
#             decoded_image = self.base64_to_image(base64_string)
#             if decoded_image.size:
#                 image_h, image_w, _ = decoded_image.shape
#                 boxes = yolo_model.predict(decoded_image)
#                 crop = []
#                 max_score = 0
#                 print('detected ', len(boxes))
#                 for box in boxes:
#                     if box.get_score() > max_score:
#                         xmin = max(int(box.xmin * image_w), 0)
#                         ymin = max(int(box.ymin * image_h), 0)
#                         xmax = max(int(box.xmax * image_w), 0)
#                         ymax = max(int(box.ymax * image_h), 0)
#                         crop = decoded_image[ymin:ymax, xmin:xmax]
#                         crop = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
#                 crop = self.preprocess_image_worker(crop)
#                 return crop
#             else:
#                 return self.process_detected_image(base64_string=base64_string)
#         except:
#             return self.process_detected_image(base64_string=base64_string)

#     def handle(self, *args, **options):
#         deep_ranking_model = self.load_deep_ranking_model()
#         yolo_model = self.load_yolo_model()
#         emb = Embedding()

#         while True:
#             queue = db.lrange(settings.IMAGE_QUEUE, 0,
#                               settings.BATCH_SIZE - 1)
#             imageIDs = []
#             # loop over the queue
#             for q in queue:
#                 q = json.loads(q.decode("utf-8"))
#                 if q['object_detect'] == True:
#                     image = self.yolo_predict(base64_string=q['image'], yolo_model=yolo_model)
#                 else:
#                     image = self.process_detected_image(base64_string=q['image'])

#                 # update the list of image IDs
#                 imageIDs.append(q["id"])
#             # check to see if we need to process the batch
#             if len(imageIDs) > 0:
#                 preds = deep_ranking_model.predict(image)
#                 for i in range(len(imageIDs)):
#                     embed = list(np.floor(np.multiply(preds[i], settings.QUANTITATION_FACTOR)))
#                     embed_str = emb.embed_to_str(embed)
#                     db.set(imageIDs[i], embed_str)
#                 # remove the set of images from our queue
#                 db.ltrim(settings.IMAGE_QUEUE, len(imageIDs), -1)

#             # sleep for a small amount
#             time.sleep(settings.SERVER_SLEEP)