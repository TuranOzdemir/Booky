
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name='home'),
    path('/logout', views.logout_user, name='logout'),
    path('/register', views.register_user, name='register'),
    path('/book/<int:book_id>', views.book_detail, name='book_detail'),

]

