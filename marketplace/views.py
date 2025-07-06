from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import UserRegisterForm, UserLoginForm, CustomUserCreationForm
from .models import Vehicle
from django.core.paginator import Paginator
import json

# Home page showing all vehicles
def home(request):
    vehicles = Vehicle.objects.all()
    cars = Vehicle.objects.filter(vehicle_type='car')[:5]  # Get the first 5 cars
    bikes = Vehicle.objects.filter(vehicle_type='bike')[:5]  # Get the first 5 bikes
    context = {
        'vehicles': vehicles,
        'cars': cars,
        'bikes': bikes,
    }
    return render(request, 'marketplace/home.html', context)

# Register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'marketplace/register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'marketplace/login.html', {'form': form})

# Logout view
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

# About page
def about(request):
    return render(request, 'marketplace/about.html')

# Contact page
def contact(request):
    return render(request, 'marketplace/contact.html')

# Dashboard for logged-in users
@login_required
def dashboard(request):
    return render(request, 'marketplace/dashboard.html')

# Page to add a vehicle
@login_required
def add_vehicle(request):
    return render(request, 'marketplace/add_vehicle.html')

# Page showing vehicles posted by the logged-in user
@login_required
def my_listings(request):
    vehicles = request.user.vehicle_set.all()
    return render(request, 'marketplace/my_listings.html', {'vehicles': vehicles})

# Page to edit user profile
@login_required
def edit_profile(request):
    return render(request, 'marketplace/edit_profile.html')

# Search vehicles with filters
def search(request):
    brand = request.GET.get('brand', '')
    model = request.GET.get('model', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    location = request.GET.get('location', '')

    vehicles = Vehicle.objects.all()

    if brand:
        vehicles = vehicles.filter(title__icontains=brand)
    if model:
        vehicles = vehicles.filter(model__icontains=model)
    if min_price:
        vehicles = vehicles.filter(price__gte=min_price)
    if max_price:
        vehicles = vehicles.filter(price__lte=max_price)
    if location:
        vehicles = vehicles.filter(location__icontains=location)

    return render(request, 'marketplace/search_results.html', {'vehicles': vehicles})

# Simple keyword search
def product_search(request):
    query = request.GET.get('query', '')
    vehicles = Vehicle.objects.filter(title__icontains=query)
    return render(request, 'marketplace/search_results.html', {'vehicles': vehicles})


def my_listings(request):
    user = request.user
    vehicles = user.vehicles.all()  # Get user's vehicles
    print(vehicles)  # Debugging: print vehicles to check if they are being fetched correctly
    return render(request, 'marketplace/my_listings.html', {'vehicles': vehicles})

def create_vehicle(request):
    # Default user (can be set to any existing user, or admin/superuser)
    default_user = User.objects.get(username='admin')  # Replace 'admin' with the desired fallback user

    # Use request.user if available, otherwise fall back to default_user
    user = request.user if request.user.is_authenticated else default_user

    # Create a new vehicle
    vehicle = Vehicle.objects.create(
        user=user,
        title="Honda Civic",  # Example dynamic value
        model="Sedan",  # Example dynamic value
        year=2020  # Example dynamic value
    )
    vehicle.save()

# Vehicle detail page
def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    return render(request, 'marketplace/vehicle_detail.html', {'vehicle': vehicle})

# Display vehicles (for pagination example)
def vehicles_view(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'marketplace/vehicles.html', {'vehicles': vehicles})

# Paginated home view
def home_view(request):
    vehicle_list = Vehicle.objects.all()
    paginator = Paginator(vehicle_list, 4)  # Show 5 per page
    page_number = request.GET.get('page')
    vehicles = paginator.get_page(page_number)
    return render(request, 'marketplace/home.html', {'vehicles': vehicles})

def vehicle_list(request):
    vehicles = Vehicle.objects.all()  # Get all vehicles from the database
    paginator = Paginator(vehicles, 4)  # Show 4 vehicles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'vehicles_list.html', {'page_obj': page_obj})

def services(request):
    return render(request, 'marketplace/services.html')
# User profile view
@login_required
def profile_view(request):
    return render(request, 'marketplace/profile.html', {'user': request.user})

# Signup page (if using custom form)
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cart')  # Redirect to cart after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'marketplace/signup.html', {'form': form})

# Custom 404 handler
def custom_404(request, exception=None):
    return render(request, 'marketplace/404.html', status=404)

def visit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    return render(request, 'marketplace/visit_vehicle.html', {'vehicle': vehicle})

def vehicle_detail(request, id):  # MUST match <int:id> in URLs
    vehicle = get_object_or_404(Vehicle, pk=id)
    return render(request, 'marketplace/vehicle_detail.html', {'vehicle': vehicle})
