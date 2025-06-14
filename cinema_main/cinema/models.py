from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    release_date = models.DateField()
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screening_time = models.DateTimeField()
    screen_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie.title} at {self.screening_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} booked {self.seats} seats for {self.screening}"

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff')
    ])

    def __str__(self):
        return f"{self.user.username} - {self.role}"
