from webbrowser import get
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from carousel.forms import ImageForm

from user.services import validate_login, getAuthUser
from .services import addImage, getGallery

def gallery(request):
    if not validate_login(request):
        return redirect('/user/login')

    user = getAuthUser(request)
    gallery = getGallery(user)

    template = loader.get_template('carousel/gallery.html')
    context = {'user': user,
               'gallery': gallery}
    return HttpResponse(template.render(context, request))

def upload(request):
    if not validate_login(request):
        return redirect('/user/login')

    user = getAuthUser(request)
    error = ""

    if request.method == 'POST':
        try:
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                addImage(request, user)
                form = ImageForm()
                error = "Upload successful."
            else:
                error = "Upload error."
        except Exception as e:
            error = "Upload error."
    else:
        form = ImageForm

    template = loader.get_template('carousel/upload.html')
    context = {'user': user,
               'form': form,
               'error': error}
    return HttpResponse(template.render(context, request))