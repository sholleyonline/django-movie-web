from django.http import HttpResponse


def movies(request):
    return HttpResponse("Hello There")

def home(request):
    return HttpResponse("Home Sweet Home")