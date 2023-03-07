from django.urls import path
from .views.trip_views import TripList, TripDetail
from .views.operator_views import *

app_name = 'trip_operator_api'

urlpatterns = [
    path('trip/<int:pk>',TripDetail.as_view(),name='detailcreate'),
    path('tripslist/',TripList.as_view(),name='listcreate'),
    path('createop/',OperatorCreate.as_view(),name='createoperator'),
    path('listoptrips/<int:pk>',OperatorDetail.as_view(),name='listoperatortrips'),
    path('viewop/',OperatorView.as_view(),name='viewop'),
    path('delop/<int:pk>',OperatorDelete.as_view(),name='delop'),
]