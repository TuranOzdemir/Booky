from django.contrib import admin
from .models import Book, Review, ReviewComment, ReviewLike, ReviewCommentLike

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(ReviewComment)
admin.site.register(ReviewLike)
admin.site.register(ReviewCommentLike)
