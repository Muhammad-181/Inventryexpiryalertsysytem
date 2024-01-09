from django.urls import path
from .import views



urlpatterns = [
    path('', views.testview, name="index"),
    path('dashboard/', views.dashboard, name="dashborad")
]