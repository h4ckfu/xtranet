from django.urls import path
from . import views

# The path can be anything any folder the .urls has to be the name of the app

urlpatterns = [
    path('', views.allblogs, name = 'allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
] 