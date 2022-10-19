from .models import Carousel, Image

def addImage(request, user):
    c = Carousel.objects.filter(user__pk=user.pk)

    if c:
        c = c[0]
    else:
        c = Carousel()
        c.user = user
        c.save()
    i = Image()
    i.carousel = c
    i.name = request.POST['name']
    i.description = request.POST['description']
    i.image = request.FILES['image']
    i.save()
    return True

def getGallery(user):
    c = Carousel.objects.filter(user__pk=user.pk)

    if c:
        c = c[0]
    else:
        c = Carousel()
        c.user = user
        c.save()
    
    i = Image.objects.filter(carousel__pk=c.pk)
    return i
