from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from api.forms import ProgramingLanguageDetectionForm
from django.utils.translation import gettext_lazy as _
from guesslang import Guess
from api.helpers.format_response import format

class ProgramingDetectView(APIView):
    parser_classes = (MultiPartParser,)
    success = _('Detect language succesfully.')
    failure = _('Detect language failed.')
    timeout = _('Detect language timeout.')

    def detect_language(self, code):
        name = Guess().language_name(code)
        return name

    def post(self, request):
        form = ProgramingLanguageDetectionForm(request.POST, request.FILES)
        if not form.is_valid():
            return format(code=422, data=[], message=self.failure, errors=form.errors)

        plain_text_code = form.cleaned_data.get('plain_text_code')

        data_response = {
            'detected_language': self.detect_language("\"\"\"{}\"\"\"".format(plain_text_code))
        }

        return format(code=200, data=data_response, message=self.success, errors=[])
