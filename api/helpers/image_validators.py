import mimetypes
import os

from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from .constants import (IMAGE_EXTENSIONS, IMAGE_MAX_SIZE, IMAGE_MIME_TYPES)


@deconstructible
class UploadedFileValidator:
    extension_code = 'invalid_extension'
    extension_message = _(
        "File extension '%(extension)s' is not allowed. "
        "Allowed extensions are: '%(allowed_extensions)s'."
    )

    mimetype_code = 'invalid_mimetype'
    mimetype_message = _(
        "File mimetype '%(mimetype)s' is not allowed. "
        "Allowed mimetypes are: '%(allowed_mimetypes)s'."
    )

    size_code = 'invalid_size'
    min_size_message = _(
        "File should be larger than %(allowed_size)s. Current size is %(size)s")
    max_size_message = _(
        "File should be smaller than %(allowed_size)s. Current size is %(size)s")

    def __init__(self, **kwargs):
        self.allowed_extensions = kwargs.pop('allowed_extensions', None)
        self.allowed_mimetypes = kwargs.pop('allowed_mimetypes', None)
        self.min_size = kwargs.pop('min_size', None)
        self.max_size = kwargs.pop('max_size', None)

    def __call__(self, value):
        extension = os.path.splitext(value.name)[1][1:].lower()
        if self.allowed_extensions and extension not in self.allowed_extensions:
            raise ValidationError(
                self.extension_message,
                code=self.extension_code,
                params={
                    'extension': extension,
                    'allowed_extensions': ', '.join(self.allowed_extensions)
                }
            )

        mimetype = mimetypes.guess_type(value.name)[0]
        if self.allowed_mimetypes and mimetype not in self.allowed_mimetypes:
            raise ValidationError(
                self.mimetype_message,
                code=self.mimetype_code,
                params={
                    'mimetype': mimetype,
                    'allowed_mimetypes': self.allowed_mimetypes
                }
            )

        size = len(value)
        if self.min_size and size < self.min_size:
            raise ValidationError(
                self.min_size_message,
                code=self.size_code,
                params={
                    'allowed_size': filesizeformat(self.min_size),
                    'size': filesizeformat(size)
                }
            )

        if self.max_size and size > self.max_size:
            raise ValidationError(
                self.max_size_message,
                code=self.size_code,
                params={
                    'allowed_size': filesizeformat(self.min_size),
                    'size': filesizeformat(size)
                }
            )


image_validator = UploadedFileValidator(allowed_extensions=IMAGE_EXTENSIONS,
                                        allowed_mimetypes=IMAGE_MIME_TYPES,
                                        max_size=IMAGE_MAX_SIZE)