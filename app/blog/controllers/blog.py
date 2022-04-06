from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/blog/index.html', {'range': range(10)})

def show(request,id):
    return render(request, 'pages/blog/index.html', {'range': range(10)})

