from django.db import models
from django.contrib.auth.models import AbstractUser
from core.base_models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)
    verification_token = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ('user', 'User'),
            ('admin', 'Admin'),
        ],
        default='user'
    )

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username



class UserProfile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profiles')
    bio = models.TextField(max_length=200)
    image = models.ImageField()
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)


class Follow(models.Model):
    pass



