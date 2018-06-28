from django.shortcuts import render
from fashion.models import Fashion
from fashion.documents import FashionDocument

def home(request):
    images = Fashion.objects.all()[48:60]
    return render(request, 'core/index.html', {'images': images })

def search(request):
    images = Fashion.objects.all()[48:60]
    return render(request, 'core/fashion_search.html', {'images': images })

def get_similarity(request, image_id):
    image = Fashion.objects.filter(image_id=image_id)
    if image:
        embedding = image.get().embedding
        results = FashionDocument.search().query("match", embedding=embedding)
        return render(request, 'core/get_similarity.html', {'results': results, 'image' : image.get()})
    return render(request, 'core/get_similarity.html', {'results': [], 'image' : []})