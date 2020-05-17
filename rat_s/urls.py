from django.urls import path
from . import views

app_name = 'rat_s'


urlpatterns = [
    path('', views.cadastrar_prestador_view, name='rat_s'),

]