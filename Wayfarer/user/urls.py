from django.urls import path
from django.views.generic import TemplateView

app_name = 'user'

urlpatterns = [
    path('',TemplateView.as_view(template_name="user/index.html")),
]