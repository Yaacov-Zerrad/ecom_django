from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50, blank=True)
    
    class Type(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'
        DIRECTOR = 'DIRECTOR', 'Director'
    type = models.CharField(max_length=50, choices=Type.choices, default=Type.STUDENT)
    
class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Type.STUDENT)
    
    
class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Type.TEACHER)
    
    
class DirectorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Type.DIRECTOR)
    
    
    
class Student(User):
    objects = StudentManager()
    class Meta:
        proxy =True
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Type.STUDENT
        return super().save(*args, **kwargs)
        
        
class Teacher(User):
    objects = TeacherManager()
    class Meta:
        proxy =True
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Type.TEACHER
        return super().save(*args, **kwargs)        
        
        
class Director(User):
    objects = DirectorManager()
    class Meta:
        proxy =True
        
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Type.DIRECTOR
        return super().save(*args, **kwargs)
            
    
