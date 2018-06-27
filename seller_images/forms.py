from django import forms

from seller_images.models import SellerImages


class SellerImageForm(forms.ModelForm):
    class Meta:
        model = SellerImages
        fields = ('image',)