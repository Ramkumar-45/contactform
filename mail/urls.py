from django.urls import path

from .views import *

urlpatterns = [
    path("", contact_form, name="contact_form"),
    path('success/', success)
]