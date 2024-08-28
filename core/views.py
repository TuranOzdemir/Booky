from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Book, Review, ReviewLike, ReviewComment, ReviewCommentLike
from .forms import SignUpForm, ReviewForm, ReviewCommentForm

def home(request):
    books = Book.objects.all()
    reviews = Review.objects.all()
    user_reviews = Review.objects.filter(user=request.user) if request.user.is_authenticated else []
    
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Error logging in - Please try again')
    
    return render(request, 'home.html', {
        'books': books,
        'reviews': reviews,
        'user_reviews': user_reviews
    })

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = book.book_reviews.all()

    # Update average rating and number of ratings
    book.average_rating = round(sum([review.book_rating for review in reviews]) / len(reviews) if reviews else 0, 3)
    book.number_of_ratings = len(reviews)
    book.save()

    for review in reviews:
        review.likes_count = review.review_likes.count()  # Corrected to use 'review_likes'
        review.user_liked = review.review_likes.filter(user=request.user).exists()  # Corrected to use 'review_likes'
        review.number_of_comments = review.review_comments.count()  # Corrected to use 'review_comments'
        review.save()
         

    return render(request, 'book_detail.html', {
        'book': book,
        'reviews': reviews,
    })

def search(request):
    query = request.POST.get('query', '')
    results = Book.objects.filter(title__icontains=query) if query else Book.objects.none()

    return render(request, 'home.html', {
        'results': results,
        'query': query,
        'books': Book.objects.all()  # To still show all books
    })

def add_review_like(request, pk):
    if request.method == 'POST':
        review = get_object_or_404(Review, pk=pk)
        if request.user.is_authenticated:
            like, created = ReviewLike.objects.get_or_create(review=review, user=request.user)
            if not created:
                like.delete()
        else:
            messages.error(request, 'You must be logged in to like a review - Please log in')
    return redirect('book_detail', book_id=review.book.id)

def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        if Review.objects.filter(book=book, user=request.user).exists():
            messages.error(request, 'You have already reviewed this book.')
        else:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.book = book
                review.user = request.user
                review.save()

                # Update book ratings
                book.number_of_ratings = Review.objects.filter(book=book).count()
                book.average_rating = round(
                    sum([review.book_rating for review in Review.objects.filter(book=book)]) / book.number_of_ratings,
                    3
                )
                book.save()

                messages.success(request, 'Your review has been added!')
            else:
                messages.error(request, 'Please correct the errors below.')
    return redirect('book_detail', book_id=book.id)

def add_review_comment(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.review = review
                comment.user = request.user
                comment.save()
                messages.success(request, 'Your comment has been added!')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            messages.error(request, 'You must be logged in to comment - Please log in')
    return redirect('book_detail', book_id=review.book.id)

def add_review_comment_like(request, pk):
    if request.method == 'POST':
        comment = get_object_or_404(ReviewComment, pk=pk)  # Corrected to use 'ReviewComment'
        if request.user.is_authenticated:
            like, created = ReviewCommentLike.objects.get_or_create(review_comment=comment, user=request.user)  # Corrected to use 'ReviewCommentLike' and 'review_comment'
            
            if not created:
                like.delete()
                messages.success(request, 'Your like has been removed!')
            else:
                messages.success(request, 'Your like has been added!')

            # Update the number of likes
            comment.number_of_likes = ReviewCommentLike.objects.filter(review_comment=comment).count()  # Corrected to use 'ReviewCommentLike' and 'review_comment'
            comment.save()
            
        else:
            messages.error(request, 'You must be logged in to like a comment - Please log in')
    return redirect('book_detail', book_id=comment.review.book.id)
