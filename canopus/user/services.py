from .models import User
from.exceptions import LoginError


def authLogin(request, u):
    request.session['user'] = u.pk
    request.session['isLoggedIn'] = True

def validate_login(request):
    if 'isLoggedIn' in request.session:
        if request.session['isLoggedIn']:
            return True
    return False

def getAuthUser(request):
    return User.objects.filter(pk=request.session['user'])[0]

def logout(request):
    request.session.flush()

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    u = User.objects.filter(email=email)
    if u.exists():
        u = u[0]
        if u.password == password:
            authLogin(request, u)
            return u
        else:
            raise LoginError