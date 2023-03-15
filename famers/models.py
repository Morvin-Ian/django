from django.db import models
import uuid 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.db import models


class Farmer(AbstractUser):
    username = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=13, blank=True, null=True)
    last_name = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    groups = models.ManyToManyField(Group, blank=True, related_name='farmer_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='farmer_set')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    class Meta:
        db_table = 'Farmer'
        verbose_name = 'Farmer'
        verbose_name_plural = 'Farmers'

    def __str__(self):
        return self.email
    

class Product(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=256)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self) -> str:
        return self.title
    
class Subsidized(models.Model):
    title = models.CharField(max_length=256)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    market_price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self) -> str:
        return self.title

