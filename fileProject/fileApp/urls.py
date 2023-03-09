from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('create', createUser, name="usercreate"),
    path('delete/<int:id>/', deleteProfile, name='deleteprofile'),
    path('update', updateProfile, name="userupdate"),
]
