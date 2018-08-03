import json
import time
import uuid
import tabby_search.settings as settings
import redis
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from api.forms import SimilarityDetectionForm
from api.helpers.format_response import format
from random import randint
from fashion.documents import FashionDocument
from api.helpers import location, get_embedding, base64_validator

db = redis.StrictRedis(host=settings.REDIS_HOST, 
    port=settings.REDIS_PORT, db=settings.REDIS_DB)

class SimilarityDetectView(APIView):
    parser_classes = (MultiPartParser,)
    success = _('Get similarity succesfully.')
    failure = _('Get similarity failed.')
    timeout = _('Get similarity timeout.')


    def post(self, request):
        form = SimilarityDetectionForm(request.POST, request.FILES)
        if not form.is_valid():
            return format(code=422, data=[], message=self.failure, errors=form.errors)

        encoded_image = form.cleaned_data.get('encoded_image')
        object_detect = form.cleaned_data.get('object_detect')
        try:
            img = get_embedding.convert_image(encoded_image)
            img, error = base64_validator.valid(img)
            if error != 0:
                return format(code=400, data=[], message=self.failure, errors=['Image can not identify'])
        except:
            return format(code=400, data=[], message=self.failure, errors=['Image can not identify'])
        embedding = get_embedding.get_emb(img, object_detect)
        if embedding is None:
            return format(code=405, data=[], message=self.timeout, errors=[])
        results = []
        try:
            results = FashionDocument.search().query("match", embedding=embedding)
        except:
            return format(code=405, data=[], message=self.timeout, errors=[])
            
        data_response = []
        for r in results:
            cur_location = location.get_random_location()
            data_response.append({
                'image_id' : r.image_id,
                'url' : r.image_path,
                'price' : randint(100000, 500000),
                'currency' : 'VND',
                'address' : cur_location['location'],
                'longitude' : cur_location['lng'],
                'lattitude' : cur_location['lat']
            })
        return format(code=200, data=data_response, message=self.success, errors=[])
