from django.db import models
from django.contrib.auth.models import User
# Register your models here.
class UserInfo(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    facebook_id=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username
# Create your models here.
