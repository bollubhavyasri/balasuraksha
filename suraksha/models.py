from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
class IssueReport(models.Model):
    user_email = models.EmailField()
    parent_email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
 
class IncidentReport(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    relationship = models.CharField(max_length=100)
    victim_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    proof_files = models.FileField(upload_to='proofs/', blank=True, null=True)

    def __str__(self):
        return f"{self.name or 'Anonymous'} - {self.description[:30]}"

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'General User'),
    ]
    
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)  # Optional username
    email = models.EmailField(unique=True)  # Login with email instead of username
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)

    USERNAME_FIELD = 'email'  # Use email for authentication
    REQUIRED_FIELDS = []  # No need to require username

    objects = CustomUserManager()

    def __str__(self):
        return self.email
