from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('', views.appofimage, name='appofimage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

]
