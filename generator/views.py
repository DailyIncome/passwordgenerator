from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):

    characters = list('qwertyuioplkjhgfdsazxcvbnm')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))

    if request.GET.get('specials'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    thepassword = ''
    for x in range(length)  :
        thepassword += random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})


def about(request):
    aboutme = 'Im Superman'
    return render(request,'generator/about.html',{'aboutme': aboutme})
