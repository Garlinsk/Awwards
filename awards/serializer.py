from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('project_title', 'project_description', 'project_image',
                  'Author', 'pub_date', 'link', 'country', 'author_profile')

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'photo',)
