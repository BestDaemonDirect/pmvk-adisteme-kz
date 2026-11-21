from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    phone = models.CharField(max_length=255, blank=True, null=True)       
    address = models.TextField(blank=True, null=True) 

    is_admin = models.BooleanField(default=False)



class TeacherInformation(models.Model):
    profile = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name="information")

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    file = models.FileField(upload_to="teacher_files/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)