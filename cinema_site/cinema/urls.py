from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list_view, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail_view, name='movie_detail'),
    path('book/<int:screening_id>/', views.book_screening_view, name='book_screening'),

]
