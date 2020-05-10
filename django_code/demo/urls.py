from django.urls import path

from . import views

urlpatterns = [path("demo", views.demo_views, name="demo")]
