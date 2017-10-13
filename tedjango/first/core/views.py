from django.shortcuts import render


# Create your views here.

def home(request):
    context = {'texto': 'Meu primeiro projeto '}
    return render(request, 'index.html', context)
