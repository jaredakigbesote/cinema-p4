from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.movie_list_view, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail_view, name='movie_detail'),
    path('book/<int:screening_id>/', views.book_screening_view, name='book_screening'),
    path('login/', auth_views.LoginView.as_view(template_name='cinema/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='movie_list'), name='logout'),
   
]

