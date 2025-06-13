from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movie, Screening, Booking
from .forms import BookingForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm

def movie_detail_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    screenings = Screening.objects.filter(movie=movie).order_by('screening_time')
    return render(request, 'cinema/movie_detail.html', {
        'movie': movie,
        'screenings': screenings,
    })

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/movie_list.html', {'movies': movies})

def book_screening_view(request, screening_id):
    screening = Screening.objects.get(id=screening_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.screening = screening
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful!')
            return redirect('movie_list') 
    else:
        form = BookingForm()

    return render(request, 'cinema/book_screening.html', {
        'form': form,
        'screening': screening
    })

    from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Login route works!")

    def __str__(self):
        return self.title

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list') 
    else:
        form = UserCreationForm()
    return render(request, 'cinema/signup.html', {'form': form})

