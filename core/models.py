from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_ratings = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0) 

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_likes = models.IntegerField(default=0)
    number_of_comments = models.IntegerField(default=0)
    book_rating = models.IntegerField(choices=[(i, i) for i in range(6)], default=0)
    #likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Reviewed {self.book.title}"
    
class Review_comments(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    number_of_likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.review.user.username}'s review on {self.review.book.title}"

class Review_likes(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('review', 'user')  # Ensure a user can only like a review once

    def __str__(self):
        return f"{self.user.username} liked {self.review.user.username}'s review on {self.review.book.title}"

# class User_Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, default='default_profile_picture.jpg')
#     bio = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     social_media = models.URLField(blank=True, null=True)
#     def __str__(self):
#         return self.user.username