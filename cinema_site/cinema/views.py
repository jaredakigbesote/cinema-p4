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

from django.shortcuts import render, redirect
from .models import Booking
from django.shortcuts import redirect
from .forms import BookingForm
from .models import Screening
from django.contrib import messages

def book_screening_view(request, screening_id):
    screening = Screening.objects.get(id=screening_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.screening = screening
            booking.save()
            messages.success(request, 'Booking successful!')
            return redirect('dashboard') 
    else:
        form = BookingForm()

    return render(request, 'cinema/book_screening.html', {
        'form': form,
        'screening': screening
    })


