from django.core.management.base import BaseCommand
import keras.backend as K
import numpy as np
import json
from keras.models import model_from_json
import tabby_search.settings as settings
import redis
import time
from seller_images.helpers import base64_decode_image
from fashion.embedding import Embedding

config = K.tf.ConfigProto()
config.gpu_options.allow_growth = True
session = K.tf.Session(config=config)

db = redis.StrictRedis(host=settings.REDIS_HOST,
                       port=settings.REDIS_PORT, db=settings.REDIS_DB)

class Command(BaseCommand):
    help = 'Cached model deep learning for generate embedding'

    def handle(self, *args, **options):
        # load json and create model
        print("Loadding model...")
        json_file = open(settings.MODEL_KERAS_JSON, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights(settings.MODEL_KERAS_WEIGHT)
        print("Loaded model from disk")
        emb = Embedding()

        while True:
            queue = db.lrange(settings.IMAGE_QUEUE, 0,
                              settings.BATCH_SIZE - 1)
            imageIDs = []
            batch = None
            # loop over the queue
            for q in queue:
                q = json.loads(q.decode("utf-8"))
                image = base64_decode_image(q["image"],
                                            settings.IMAGE_DTYPE,
                                            (1, settings.IMAGE_HEIGHT, settings.IMAGE_WIDTH,
                                             settings.IMAGE_CHANS))
                # check to see if the batch list is None
                if batch is None:
                    batch = image
                else:
                    batch = np.vstack([batch, image])

                # update the list of image IDs
                imageIDs.append(q["id"])

            # check to see if we need to process the batch
            if len(imageIDs) > 0:
                preds = loaded_model.predict(batch)
                for i in range(len(imageIDs)):
                    embed = list(np.floor(np.multiply(preds[i], settings.QUANTITATION_FACTOR)))
                    embed_str = emb.embed_to_str(embed)
                    db.set(imageIDs[i], embed_str)
                # remove the set of images from our queue
                db.ltrim(settings.IMAGE_QUEUE, len(imageIDs), -1)

            # sleep for a small amount
            time.sleep(settings.SERVER_SLEEP)