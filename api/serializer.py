from rest_framework import serializers
from .models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Site
        fields=['image', 'url','owner', 'name',  'date_posted']
