from django.urls import path
app_name = 'api'
from api.views.similarity_detect import SimilarityDetectView
from api.views.language_detect import ProgramingDetectView

urlpatterns = [
    path('similarity_detect',
         SimilarityDetectView.as_view(), name='similarity-detect'),
    path('programing_language_detect',
         ProgramingDetectView.as_view(), name='programing-language-detect'),
]
