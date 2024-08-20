from django.shortcuts import render
from .models import Book, Review
from django.contrib.auth.models import User

def home(request):
    books = Book.objects.all()
    reviews = Review.objects.all()
    if User.is_authenticated:
        user_reviews = Review.objects.filter(user=request.user)
        return render(request, 'home.html', {'books': books, 'reviews': reviews, 'user_reviews': user_reviews})
    else:
        user_reviews = None
    
        
        
    return render(request, 'home.html', {'books': books, 'reviews': reviews, 'user_reviews': user_reviews})