from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from PIL import Image
from tinymce.models import HTMLField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='profile_pics/', blank=True, default='profile_pics/default.jpg')
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
        return self.about

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
class Projects(models.Model):
    project_title = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to='images/', default='images/default.jpg')
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    author_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, default='1')
    link = models.URLField()
   

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects

    @classmethod
    def get_by_author(cls, Author):
        projects = cls.objects.filter(Author=Author)
        return projects

    @classmethod
    def get_project(request, id):
        try:
            project = Projects.objects.get(pk=id)

        except ObjectDoesNotExist:
            raise Http404()

        return project

    def __str__(self):
        return self.project_title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Project'
        verbose_name_plural = 'Projects'
