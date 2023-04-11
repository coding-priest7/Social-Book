from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# Create your models here.
# this is where we create our django models which we can use it as a database

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile_images', default='blank-profile-picture.jpg')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    # @property
    # def get_photo_url(self):
    #     if self.photo and hasattr(self.photo, 'url'):
    #         return self.photo.url
    #     else:
    #         return "static/assets/images/post/img4.jpg"

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


