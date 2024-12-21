from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Header(models.Model):
    logo=models.ImageField(upload_to="header/")
    avatar=models.ImageField(upload_to="header/")
    position=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    email=models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)
    available=models.BooleanField(default=True)


class Education(models.Model):
    specialization=models.CharField(max_length=100)
    institution=models.CharField(max_length=100)
    subjects=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.specialization} {self.institution}"
    class Meta:
        ordering=['start_date']


class About(models.Model):
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


class Experience(models.Model):
    position=models.CharField(max_length=150)
    company=models.CharField(max_length=150)
    logo=models.ImageField(upload_to="company/")
    description=models.TextField(max_length=400)
    created_at=models.DateTimeField(auto_now_add=True)
    start_date=models.DateField()
    end_date=models.DateField(null=True, blank=True)
    class Meta:
        ordering=['start_date']


class Skill(models.Model):
    image=models.ImageField(upload_to="skills/")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.image.name}"
    class Meta:
        ordering=['created_at']
class Project(models.Model):
    image=models.ImageField(upload_to="project/")
    title=models.CharField(max_length=150)
    description=models.TextField(max_length=250)
    link=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        ordering=['created_at']
class SocialNetwork(models.Model):
    title=models.CharField(max_length=150)
    link=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="socials/", blank=True, null=True)
    priority=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)], default=0)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        ordering=['priority']