"""
URL configuration for mvp_alpha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', main_views.home, name='home'), # Homepage
    path('reading_journey/', include('reading_journey.urls')),
    path('review_platform/', include('review_platform.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# The admin site works with the following paths
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('reading_journey.urls')),
    path('', views.book_list, name='book_list'),
    path('book/', views.book_detail, name='book_detail'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('', include('review_platform.urls')),
]
"""