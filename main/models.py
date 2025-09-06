import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('cleat', 'Cleat'),
        ('glove', 'Glove'),
        ('shin guard', 'Shin guard'),
        ('sock', 'Sock'),
        ('jersey', 'Jersey'),
        ('football', 'Football')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    @property
    def is_popular(self):
        return self.views > 20
    
    def increment_views(self):
        self.views += 1
        self.save()
