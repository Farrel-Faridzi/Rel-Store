import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('cleats', 'Cleats'),
        ('gloves', 'Gloves'),
        ('shin guards', 'Shin guards'),
        ('socks', 'Socks'),
        ('jerseys', 'Jerseys'),
        ('football', 'Football')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_popular(self):
        return self.views > 20
    
    def increment_views(self):
        self.views += 1
        self.save()


class Employee(models.Model):
    
    name= models.CharField(max_length=255)
    age = models.IntegerField()
    persona = models.TextField()