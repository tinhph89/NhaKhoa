
from django.urls import path
from accounts import views

# url for home pages
urlpatterns = [
    path('', views.login, name = 'login'),
]