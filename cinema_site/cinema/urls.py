from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list_view, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail_view, name='movie_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
