from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    createDate = models.DateTimeField(auto_now_add=True, null=True)
    completeDate = models.DateTimeField(blank=True, null=True)
    importance = models.BooleanField(default=False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.title} | {self.user} "