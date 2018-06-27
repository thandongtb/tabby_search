from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from fashion.models import Fashion
from seller_images.models import SellerImages
from seller_images.forms import SellerImageForm
from fashion.documents import FashionDocument

def home(request):
    images = Fashion.objects.all()[48:60]
    return render(request, 'core/index.html', {'images': images })

def get_similarity(request, image_id):
    image = Fashion.objects.filter(image_id=image_id)
    if image:
        embedding = image.get().embedding
        results = FashionDocument.search().query("match", embedding=embedding)
        return render(request, 'core/search.html', {'results': results, 'image' : image.get()})
    return render(request, 'core/search.html', {'results': [], 'image' : []})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = SellerImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SellerImageForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })