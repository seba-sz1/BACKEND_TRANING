from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return f"{self.title} | {self.owner}"
    
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if kwargs['created']:
        Token.objects.create(user=kwargs['instance'])
    # print("Receiver działa")
    # print(kwargs)