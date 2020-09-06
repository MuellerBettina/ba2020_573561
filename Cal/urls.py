from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar),
    path('get/<id>', views.get_event, name='get_event'),
    path('delete/<id>', views.delete_event, name='delete_event'),
]