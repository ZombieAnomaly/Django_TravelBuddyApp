from django.shortcuts import render, redirect, HttpResponse
import hashlib, datetime
from apps.travel_app.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'travel_app/index.html')

def home(request):
    if 'id' not in request.session:
        redirect(index)
    user = User.objects.get(id=request.session['id'])
    trips = user.trips.all()
    other_trips = TravelPlan.objects.all()
    context = {
        'username':user.username,
        'user': user,
        'trips':trips,
        'other_trips':other_trips
    }
    return render(request,'travel_app/home.html', context)

def register(request):
    if request.POST:
        name = request.POST['name']
        username = request.POST['username']
        password = hashlib.md5(request.POST['password'].encode()).hexdigest()

        errors = User.objects.validate_Registration(request.POST)

        if len(errors):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            return redirect(index)
        else:
            u = User.objects.create(name = name, username = username, password = password)
            request.session['id'] = u.id
            return redirect(home)

def login(request):
    if request.POST:
        username = request.POST['login_username']
        password = hashlib.md5(request.POST['login_password'].encode()).hexdigest()
        postdata = {
            'login_username': username,
            'login_password': password
        }
        errors = User.objects.Validate_Login(postdata)

        if len(errors):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            return redirect(index)
        else:
            u = User.objects.get(username = username, password=password)
            request.session['id'] = u.id
            return redirect(home)

def logout(request):
    if 'id' in request.session:
        request.session.clear()
    return redirect(index)

def new(request):
    return render(request, 'travel_app/new_trip.html')

def add(request):
    if request.POST:
        destination = request.POST['destination']
        description = request.POST['description']
        date_to = request.POST['date_to']
        date_from = request.POST['date_from']

        errors = TravelPlan.objects.validate(request.POST)

        if len(errors):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            return redirect(new)
        else:
            u = User.objects.get(id=request.session['id'])
            travel_plan = TravelPlan.objects.create(destination = destination, description = description, date_to = date_to, date_from = date_from, owner = u)
            travel_plan.users.add(u)
            messages.add_message(request, messages.INFO, 'Plans succesfully added!')
            return redirect(home)

def destination(request,destination_id):
    trip = TravelPlan.objects.get(id=destination_id)
    context = {
        'trip':trip
    }
    return render(request, 'travel_app/destination.html', context)

def join(request, trip_id):
     trip = TravelPlan.objects.get(id=trip_id)
     u = User.objects.get(id=request.session['id'])
     trip.users.add(u)
     return redirect(home)