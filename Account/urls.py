from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('index', views.index, name='index'),
    path('transfer', views.transfer, name='transfer'),
    path('show/<str:id>', views.show, name='show'),
]
