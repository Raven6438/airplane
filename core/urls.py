from django.urls import path
from django.views.generic import RedirectView

from core import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='home'), name='redirect_to_home'),
    path('home/', views.home, name='home'),
]