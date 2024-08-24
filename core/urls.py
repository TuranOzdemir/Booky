
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name='home'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('book/<int:book_id>', views.book_detail, name='book_detail'),
    path('search', views.search, name='search'),
    path('add_review_like/<int:pk>/', views.add_review_like, name='add_review_like'),
    path('add_review/<int:book_id>/', views.add_review, name='add_review'),

]

