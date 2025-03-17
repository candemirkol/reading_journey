from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('reading-journey/', include('reading_journey.urls')), 
    path('review-platform/', include('review_platform.urls')),
]