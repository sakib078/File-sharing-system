from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include
from django.views.generic import RedirectView
from users import views as user_views

urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),  # Redirect / to login page
    path('admin/', admin.site.urls),
    path('fileshare/', include('fileshare.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='Login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='Logout'),
]
