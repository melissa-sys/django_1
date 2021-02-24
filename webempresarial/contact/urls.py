from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.page, name='contact')
]
