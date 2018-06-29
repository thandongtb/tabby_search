from django import forms
from api.helpers.image_validators import image_validator

class SimilarityDetectionForm(forms.Form):
    # image = forms.FileField(validators=[image_validator])
    encoded_image = forms.CharField(required=True)
    object_detect = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data

class ProgramingLanguageDetectionForm(forms.Form):
    plain_text_code = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data