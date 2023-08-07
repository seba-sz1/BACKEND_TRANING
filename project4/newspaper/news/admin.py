from django.contrib import admin
from .models import Article

class Date(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Article, Date)
