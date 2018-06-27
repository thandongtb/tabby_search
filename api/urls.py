from django.urls import path
app_name = 'api'
from api.views.similarity_detect import SimilarityDetectView

urlpatterns = [
    path('similarity_detect',
         SimilarityDetectView.as_view(), name='similarity-detect'),
]
