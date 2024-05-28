# recognition/urls.py

from django.urls import path
from .views import add_new_user, get_id_info, get_all

urlpatterns = [
    path('add_new_user/', add_new_user, name='add_new_user'),
    path('get_id_info/', get_id_info, name='get_id_info'),
    path('get_all/', get_all, name='get_all'),
]
