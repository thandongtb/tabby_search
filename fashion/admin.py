from django.contrib import admin
from fashion.models import Fashion
from watson.admin import SearchAdmin

class FashionAdmin(SearchAdmin):
    search_fields = ("image_path", "embedding",)  # A tupl

# Register your models here.
admin.site.register(Fashion, FashionAdmin)

