from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "blockit"

urlpatterns = [
    path('', views.home, name='blockit-home'),
    path('about/', views.about, name='blockit-about'),
    path('login/', auth_views.LoginView.as_view(template_name='blockit/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]