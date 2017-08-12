from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    random_string = get_random_string(length=32)
    if request.method == "POST":
        request.session['counter'] += 1
        context = {
        'word': random_string,
        }
    else:
        request.session['counter'] = 0
        context = {
        'word': "",
        }
    return render(request,'random_word/index.html', context)
