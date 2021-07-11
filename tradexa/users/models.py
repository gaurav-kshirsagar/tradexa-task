from django.db import models

# Create your models here.
class PostUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254,db_index = True)
    username = models.CharField(max_length=200,db_index=True,unique=True)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username

class Post(models.Model):
    username = models.ForeignKey(PostUser,
                             on_delete=models.CASCADE,
                             related_name='posts',)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

        