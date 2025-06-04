import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ParticipantProfile
import csv

# ✅ CSRF endpoint
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'message': 'CSRF cookie set'})

# ✅ Landing Page
def landing_view(request):
    return render(request, 'competition/landing.html')

# ✅ Register View (secured, CSRF via frontend)
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            username = data.get('username')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirm_password')

            if not username:
                return JsonResponse({'error': "Username is required."}, status=400)
            elif not password or not confirm_password:
                return JsonResponse({'error': "Password fields cannot be empty."}, status=400)
            elif password != confirm_password:
                return JsonResponse({'error': "Passwords do not match."}, status=400)
            elif User.objects.filter(username=username).exists():
                return JsonResponse({'error': "Username already taken."}, status=400)

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name or "",
                last_name=last_name or ""
            )
            return JsonResponse({'message': "Registration successful"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': "Invalid JSON"}, status=400)

    return JsonResponse({'error': "Only POST method allowed"}, status=405)

# ✅ Login View (session-based)
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({'message': "Login successful"}, status=200)
            return JsonResponse({'error': "Invalid credentials"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': "Invalid JSON"}, status=400)

    return JsonResponse({'error': "Only POST method allowed"}, status=405)

# ✅ Dashboard View (requires login)
@login_required
def dashboard_view(request):
    return JsonResponse({'message': f'Welcome, {request.user.username}!'}, status=200)

# ✅ Logout
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out'}, status=200)

# ✅ Export CSV
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
