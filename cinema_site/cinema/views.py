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
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cinema/register.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'cinema/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'cinema/dashboard.html')

    from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import BookingForm
from .models import Screening
from django.contrib import messages

@login_required
def book_screening_view(request, screening_id):
    screening = Screening.objects.get(id=screening_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
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


