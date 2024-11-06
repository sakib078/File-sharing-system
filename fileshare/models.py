from django.db import models
from django.contrib.auth.models import User


class file(models.Model):
    tittle = models.CharField(max_length=255)
    document = models.FileField(default='default value')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.BinaryField(default=bytes([0]))
    
class SharedFile(models.Model):
    file = models.ForeignKey(file, on_delete=models.CASCADE)
    shared_by = models.ForeignKey(User, related_name='shared_by', on_delete=models.CASCADE)
    shared_with = models.ForeignKey(User, related_name='shared_with', on_delete=models.CASCADE)
