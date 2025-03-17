from django.urls import path
from . import views


app_name = 'review_platform'

urlpatterns = [
    path('', views.review_platform_home, name='review_platform_home'),
    path('book_list/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
]