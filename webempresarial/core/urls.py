from django.urls import path
from core import views as core_views
from Services import views as ser_views
from blog import views as blog_views
from pages import views as page_views
from contact import views as cont_views

urlpatterns = [
    path('', core_views.home, name="index"),

    path('about/', core_views.about, name="about"),

    path('services/', ser_views.services, name="services"),

    path('store/', core_views.store, name="store"),

    path('page/', page_views.page, name="sample"),

    path('contact/', cont_views.contact, name="contact"),

]
