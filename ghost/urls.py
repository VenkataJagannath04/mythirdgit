from django.urls import path
from ghost.views import *
app_name='Something'

urlpatterns=[
    path('Jinja_print/', Jinja_print, name='Jinja_print'),
]