from rest_framework import serializers
from students.models import Student as stm

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = stm
        fields = ('name','cod','course','id')
