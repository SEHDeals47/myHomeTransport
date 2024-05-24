from django.urls import path
from paid_page import views

urlpatterns = [
    path('',views.home,name='main'),
]