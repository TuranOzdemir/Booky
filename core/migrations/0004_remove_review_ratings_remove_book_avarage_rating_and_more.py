# Generated by Django 5.1 on 2024-08-22 00:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_ratings_book_alter_review_book_review_ratings_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='ratings',
        ),
        migrations.RemoveField(
            model_name='book',
            name='avarage_rating',
        ),
        migrations.AddField(
            model_name='book',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='book_rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ratings'),
        ),
        migrations.AddField(
            model_name='review',
            name='number_of_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.CreateModel(
            name='Review_likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_likes', to='core.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('review', 'user')},
            },
        ),
        migrations.DeleteModel(
            name='Review_Ratings',
        ),
    ]
