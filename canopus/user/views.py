from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


from .forms import LoginForm
from .services import login, logout, validate_login

def loginView(request):

    error = ""

    if validate_login(request):
        return redirect('/gallery')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                login(request)
                return redirect('/gallery')
            except Exception as e:
                error = "Authentification error. Check your credentials."
    else:
        form = LoginForm()

    template = loader.get_template('user/login.html')
    context = {'form': form,
               'error': error,}
    return HttpResponse(template.render(context, request))

def logoutView(request):
    logout(request)
    return redirect("..")