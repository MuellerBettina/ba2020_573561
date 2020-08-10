"""BlockIt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

import blockit
from timeblocks.views import showTimeBlock
from users import views as user_views
from timeblocks import views as timeblock_views
from blockit import views as blockit_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('add/', timeblock_views.addTimeBlock, name='addTimeBlock'),
    path('showTimeBlock/<int:block_id>/', timeblock_views.showTimeBlock, name='showTimeBlock'),
    path('deleteTimeBlock/<int:block_id>/', timeblock_views.deleteTimeBlock, name='deleteTimeBlock'),
    path('scheduleTimeBlock/<int:block_id>/', timeblock_views.ScheduleTimeBlock.as_view(template_name='timeblocks/pickdatetime.html'), name='scheduleTimeBlock'),
    path('timeblocks/', timeblock_views.timeBlockList, name='timeBlockList'),
    #path('calendar/', include('blockit.urls')),
    path('calendar/', include('Cal.urls')),
    path('', include('blockit.urls')),
]
