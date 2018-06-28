from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from api.forms import SimilarityDetectionForm
import numpy as np
from keras.preprocessing import image as keras_image
from api.helpers.format_response import format
from PIL import Image
from keras.applications.inception_v3 import preprocess_input
from tabby_search.settings import IMAGE_WIDTH, IMAGE_HEIGHT
from seller_images.helpers import base64_decode_image, base64_encode_image
import tabby_search.settings as settings
import redis
import uuid
import json
import time
from random import randint
from fashion.documents import FashionDocument
from api.helpers import location
import base64
from io import BytesIO

db = redis.StrictRedis(host=settings.REDIS_HOST,
	port=settings.REDIS_PORT, db=settings.REDIS_DB)

class SimilarityDetectView(APIView):
    parser_classes = (MultiPartParser,)
    success = _('Get similarity succesfully.')
    failure = _('Get similarity failed.')
    timeout = _('Get similarity timeout.')

    def preprocess_image_worker(self, path):
        img = Image.open((path)).convert('RGB')
        img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))

        x = keras_image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        return x

    def post(self, request):
        form = SimilarityDetectionForm(request.POST, request.FILES)
        if not form.is_valid():
            return format(code=422, data=[], message=self.failure, errors=form.errors)

        encoded_image = form.cleaned_data.get('encoded_image')
        image_decoded = BytesIO(base64.b64decode(encoded_image))
        image = self.preprocess_image_worker(image_decoded)
        image = image.copy(order="C")
        k = str(uuid.uuid4())
        image = base64_encode_image(image)
        d = {"id": k, "image": image}
        db.rpush(settings.IMAGE_QUEUE, json.dumps(d))
        start_time = time.time()
        results = []
        while True:
            output = db.get(k)
            if output is not None:
                embedding = output.decode("utf-8")
                results = FashionDocument.search().query("match", embedding=embedding)
                db.delete(k)
                break
            if (time.time() - start_time > 10):
                return format(code=405, data=[], message=self.timeout, errors=[])

            time.sleep(settings.CLIENT_SLEEP)
        data_response = []
        for r in results:
            cur_location = location.get_random_location()
            data_response.append({
                'image_id' : r.image_id,
                'url' : r.image_path,
                'price' : randint(1000, 10000),
                'currency' : 'VND',
                'address' : cur_location['location'],
                'longitude' : cur_location['lng'],
                'lattitude' : cur_location['lat']
            })
        return format(code=200, data=data_response, message=self.success, errors=[])