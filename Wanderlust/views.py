"""
Views of the app are created here
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import WanderlustUserForm
from .models import Trip
from .forms import Addtrip



def home(request):
    """
    defines the home view of the app
    """
    return render(request, 'Home.html')

# def login(request):
#     return render(request, 'login.html')

# def signup(request):
    # return render(request, 'signup.html')

def contact(request):
    """
    Renders contact page.
    """
    return render(request, 'contact.html')

def signup_view(request):
    """
    Renders signup page.
    """
    if request.method == "POST":
        form = WanderlustUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            dob = form.cleaned_data.get('dob')
            # address = form.cleaned_data.get('address')
            phone_number = form.cleaned_data.get('phone_number')
            user = form.save(commit=False)  # Save the user
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            # user.address = address
            user.dob = dob
            user.phone_number = phone_number
            user.save()  # Now save the user object
            print(form.data)
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                print(f"user.is_authenticated: {user.is_authenticated}")
                print({"username": username, "password": raw_password})
                login(request, user)
                print(form.data)
                return redirect('home')
    else:
        form = WanderlustUserForm()
    return render(request, 'Signup.html', {'form': form})

def logout_view(request):
    """
    bring back to home after logout.
    """
    logout(request)
    return redirect('home')  # Redirect to your desired page

def login_view(request):
    """
    Renders login page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Create the form
        if form.is_valid():  # Validate the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Authenticate user
            if user is not None:
                login(request, user)  # Log in the user
                return redirect('home')  # Redirect to the homepage or any other desired page
              # Display error message
        else:
            print("Form errors: ", form.errors)
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()  # Create an empty form for GET requests

    context = {'form': form, 'is_logged_in': request.user.is_authenticated,
               'username': request.user.username if request.user.is_authenticated else None}
    return render(request, 'login.html', context)  # Render the login template

def trips(request):
    """
    Renders upcoming trips page.
    """
    local_trips = Trip.objects.all()
    return render(request, 'trips.html', {'trips': local_trips})

@login_required
def join_trip(request, trip_id):
    """
    view to join trips.
    """
    trip = Trip.objects.get(pk=trip_id)
    user = request.user

    if  trip.participants.count() >= trip.max_participants:
        # Trip is full, display a message or redirect to an appropriate page
        print("members full")
        messages.error(request, 'Sorry, this trip is already at its maximum capacity.')
        return redirect('trips')
        # return redirect('jointrip', trip_id)  # Redirect to the trip detail page
    # Trip is not full, allow user to join
    if user not in trip.participants.all():
        trip.participants.add(user)
        print("you are  joined")
        messages.success(request, 'You have successfully joined the trip!')
    else:
        # User already joined, display a message or redirect to an appropriate page
        messages.error(request, 'You have already joined this trip.')
        print("already joined")
    return redirect('trips')
@login_required
def add_trip(request):
    """
    Renders host a trip page.
    """
    if request.method == 'POST':
        form = Addtrip(request.POST, request.FILES)
        print("yes")
        if form.is_valid():
            user = request.user
            title = form.cleaned_data.get('title')
            image = form.cleaned_data.get('image')
            description = form.cleaned_data.get('description')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            destination = form.cleaned_data.get('destination')
            travel_mode = form.cleaned_data.get('travel_mode')
            accomodation_type = form.cleaned_data.get('accommodation_type')
            estimated_budget = form.cleaned_data.get('estimated_budget')
            max_participants = form.cleaned_data.get('max_participants')
            trip =form.save(commit=False)
            trip.title = title
            trip.image = image
            trip.description = description
            trip.start_date = start_date
            trip.end_date = end_date
            trip.destination = destination
            trip.travel_mode = travel_mode
            trip.accommodation_type = accomodation_type
            trip.estimated_budget = estimated_budget
            trip.max_participants = max_participants
            trip.user = user
            trip.save()
            return redirect('trips')
    else:
        # print(form.cleaned_data)
        form = Addtrip()
    return render(request, 'addtrip.html', {'form': form})
@login_required
def hosting_trips(request):
    """
    Renders trips with you as host.
    """
    hostingtrips = Trip.objects.filter(user=request.user)
    return render(request, 'hostingtrips.html', {'trips': hostingtrips})
def delete_trip(request, trip_id):
    """
    Renders upcoming trip page after deleting a trip.
    """
    trip = get_object_or_404(Trip, pk=trip_id)
  # Check if the user has permission to delete this trip (e.g., is the trip owner)
    if request.user.is_authenticated and trip.user == request.user:
        trip.delete()
        messages.success(request, 'Trip successfully deleted!')
    else:
        messages.error(request, 'You are not authorized to delete this trip.')
    return redirect('hostingtrips')  # Redirect to trip listings page after deletion or error

def modify_trip(request, trip_id):
    """
    Renders modify trip page.
    """
    trip = get_object_or_404(Trip, pk=trip_id)
    if request.method == 'POST':
        initial_data = {
            'title': trip.title,
            'destination': trip.destination,
            # Add other fields and their corresponding trip object attributes
        }
        form = Addtrip(request.POST, request.FILES, instance=trip, initial=initial_data)
        if form.is_valid():
            form.save()
            return redirect('trips')
    else:
        form = Addtrip(instance=trip)
    return render(request, 'modifytrip.html', {'form': form})

def joined_trips(request):
    """
    Renders joined trips page.
    """
    joinedtrips = Trip.objects.filter(participants=request.user)
    return render(request, 'joined_trips.html', {'trips': joinedtrips})

def trip_detail(request, trip_id):
    """
    Renders details page of people who joined your trip.
    """
    trip = Trip.objects.get(pk=trip_id)
    if request.user.is_authenticated and trip.user == request.user:
        participants = trip.participants.all()
        context = {'trip': trip, 'participants': participants}
    return render(request, 'trip_detail.html', context)

def leave_trip(request, trip_id):
    """
    Renders joined trips page after leaving a trip.
    """
    trip = get_object_or_404(Trip, pk=trip_id)
  # Check if the user is actually a participant in the trip
    if request.user in trip.participants.all():
        trip.participants.remove(request.user)
        messages.success(request, 'You have successfully left the trip!')
    return redirect('joinedtrips')

def tips(request):
    """defining tips"""
    return render(request, 'tips.html')
