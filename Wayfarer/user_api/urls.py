from django.urls import path
from .views.nomad_views import NomadCreate

app_name = 'user_api'

urlpatterns = [
    path('nomadcreate/',NomadCreate.as_view(),name='nomadcreate'),
    # path('',TrekList.as_view(),name='listcreate'),
]