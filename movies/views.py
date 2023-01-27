from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie



#data =  {'movies': ['movie1','movie2']}
""" data =  {'movies': [
    {
        'id':5,
        'title':'Jaws',
        'year':1669
    },
    {
        'id':6,
        'title':'Sharknado',
        'year':1600
    },
    {
        'id':7,
        'title':'The Meg',
        'year':2000
    }
    
    ]} """
#def movies(request):
#    return HttpResponse("Hello There")

"""def movies(request):
    return render(request, 'movies/movies.html',data)"""
def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html',{'movies':data})    
def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/details.html',{'movie':data})

def home(request):
    return HttpResponse("Home Sweet Home")

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    movie.delete()
    return HttpResponseRedirect('/movies')

