from django.urls import path
from things.views import index

urlpatterns = [
    path('', index, name='index'),
]

