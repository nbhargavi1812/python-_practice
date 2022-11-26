from rest_framework import serializers
from firstapp.models import student

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=('student_id','student_name','student_mobileno')