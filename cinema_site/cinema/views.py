from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import Movie, Screening

def movie_detail_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    screenings = Screening.objects.filter(movie=movie).order_by('screening_time')
    return render(request, 'cinema/movie_detail.html', {
        'movie': movie,
        'screenings': screenings,
    })

from django.shortcuts import render
from .models import Movie

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/movie_list.html', {'movies': movies})
