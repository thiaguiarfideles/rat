from django.urls import path
from . import views


app_name = 'app_frequencia'

urlpatterns = [
    path('', views.frequencia_view, name = 'frequencia'),

]