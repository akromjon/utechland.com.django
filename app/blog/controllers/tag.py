from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/home/index.html', {'range': range(10)})

def show(request,slug):
    return render(request, 'pages/home/index.html', {'range': range(10)})

