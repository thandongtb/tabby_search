from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class SellerImages(models.Model):
    """
    Model for fashion
    """
    image = models.FileField(upload_to='media/images/')
    pub_date = models.DateTimeField('pub_date', auto_now=True)
    enable = models.BooleanField('enable', default=True)
