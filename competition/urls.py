from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
    path('', views.landing_view, name='landing'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('export-participants/', views.export_participants_csv, name='export_participants'),

    # Password Reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='competition/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='competition/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='competition/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='competition/password_reset_complete.html'), name='password_reset_complete'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
