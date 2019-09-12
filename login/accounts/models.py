from django.db import models

class post(models.Model):
    name=models.CharField(max_length=100)
    des=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='pics')