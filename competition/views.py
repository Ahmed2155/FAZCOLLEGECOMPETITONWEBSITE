from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Landing Page
def landing_view(request):
    return render(request, 'competition/landing.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username:
            messages.error(request, "Username is required.")
        elif not password or not confirm_password:
            messages.error(request, "Password fields cannot be empty.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name or "",
                last_name=last_name or ""
            )
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')

    return render(request, 'competition/register.html')


# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'competition/login.html')


# Dashboard View (Login Required)
@login_required
def dashboard_view(request):
    return render(request, 'competition/dashboard.html', {'user': request.user})


# Logout View
def logout_view(request):
    logout(request)
    return redirect('landing')

import csv
from django.http import HttpResponse
from .models import ParticipantProfile

def export_participants_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="participants.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Grade', 'School', 'Parent Name', 'Phone', 'Date'])

    for profile in ParticipantProfile.objects.all():
        writer.writerow([
            profile.user.username,
            profile.grade,
            profile.school_name,
            profile.parent_name,
            profile.phone_number,
            profile.selected_competition_date
        ])

    return response
