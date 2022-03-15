from django.urls import path
from tango import views
app_name = 'tango'
urlpatterns = [
    path('', views.index, name='index'),
]
