from django.contrib import admin
from .models import Book, Review, Review_likes, Review_comments

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Review_likes)
admin.site.register(Review_comments)

