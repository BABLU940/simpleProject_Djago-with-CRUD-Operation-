from rest_framework import serializers
from .models import *

class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 

class Sectionsserializers(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__' 