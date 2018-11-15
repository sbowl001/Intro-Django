from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from django.utils import timezone 
# Create your models here.

class Author(models.Model):
    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    dob = models.DateField( auto_now = False, default = timezone.now)

class Note (models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField( max_length = 30)
    body = models.TextField( blank = True )
    # author = models.CharField( max_length = 25)
    author = models.ForeignKey( Author, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now = True)
    completed = models.BooleanField(default = False)
    urgent = models.BooleanField(default =False)
    created_at = models.DateTimeField(default = timezone.now)
    last_modified = models.DateTimeField(default= timezone.now)

  

# class NoteAdmin(admin.ModelAdmin):
	# readonly_fields=('created_at', 'last_modified')