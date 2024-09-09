from django.shortcuts import render, get_object_or_404
from .models import Blog

def about(request):
    return render(request, 'blogs/about.html')

def page_detail(request, page_id):
    blog = get_object_or_404(Blog, id=page_id)  # Obtener el blog específico por ID
    return render(request, 'blogs/page_detail.html', {'blog': blog})

def pages(request):
    blogs = Blog.objects.all()  # pylint: disable=no-member
    return render(request, 'blogs/pages.html', {'blogs': blogs})
