from django import forms
from api.helpers.image_validators import image_validator


class SimilarityDetectionForm(forms.Form):
    image = forms.FileField(validators=[image_validator])

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data
