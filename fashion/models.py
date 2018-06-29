from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Fashion(models.Model):
    """
    Model for fashion
    """
    image_id = models.CharField('image_id', max_length = 500, blank=True)
    image_path = models.CharField('image_path', max_length = 1000, blank=True)
    embedding = models.TextField('embedding', blank=True)
    pub_date = models.DateTimeField('pub_date', auto_now=True)
    enable = models.BooleanField('enable', default=True)
