from django.db import models

# Create your models here.

class SignUp(models.Model):
    # created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name=models.CharField(max_length=254, blank=True, null=True)
    email=models.EmailField(max_length=254, blank=True, null=True)
    password=models.CharField(max_length=254, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted=models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    
    def __str__(self):
        return self.username









