from django.db import models

# Create your models here.

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Recent_Activity(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    u_file_type = models.CharField(max_length=10)
    ext_data = models.TextField()