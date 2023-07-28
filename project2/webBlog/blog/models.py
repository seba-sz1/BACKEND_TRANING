from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.title} | {self.date}"
