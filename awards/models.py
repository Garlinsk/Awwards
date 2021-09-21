from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pics/', blank=True, default='profile_pics/default.jpg')
    about = models.TextField(blank=True)

    def save_profile(self):
        self.save()

        img = open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return  self.about

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
