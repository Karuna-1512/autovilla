from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_vehicle, name='add_vehicle'),
    path('my-listings/', views.my_listings, name='my_listings'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('signup/', views.signup, name='signup'),
    path('services/', views.services, name='services'),  
    path('vehicles/', views.vehicles_view, name='vehicles'),
    path('search/', views.search, name='vehicle_search'),  # Fix search URL
    path('visit/<int:vehicle_id>/', views.visit_vehicle, name='visit_vehicle'),
    path('profile/', views.profile_view, name='profile'),
    path('vehicles/<int:id>/', views.vehicle_detail, name='vehicle_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
