from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def about(request):
    my_context = {
        "my_list": [1,2,3,4,5,6]
    }
    return render(request, 'about.html', {})
