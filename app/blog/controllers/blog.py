from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/blog/index.html', {'range': range(100)})

def show(request,slug):
    return render(request, 'pages/blog/show.html')

