from django.contrib import admin
from .models import Movie, Screening, Booking, StaffProfile

admin.site.register(Movie)
admin.site.register(Screening)
admin.site.register(Booking)
admin.site.register(StaffProfile)
