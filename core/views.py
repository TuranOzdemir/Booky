from django.shortcuts import render, redirect
from .models import Book, Review
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm



def home(request):
    books = Book.objects.all()
    reviews = Review.objects.all()
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        # If user is found
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.error(request, ('Error logging in - Please try again'))
            return redirect('home')
    else:
        if request.user.is_authenticated:
            user_reviews = Review.objects.filter(user=request.user)
        else:
            user_reviews = []
        return render(request, 'home.html', {'books': books, 'reviews': reviews, 'user_reviews': user_reviews})
    
    
    
    
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Successfully registered!'))
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = Review.objects.filter(book=book)
    for review in reviews:
        review.stars = range(review.rating)
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})
