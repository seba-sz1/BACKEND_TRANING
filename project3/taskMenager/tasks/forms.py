from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','desc', 'importance',)
        # exludes = ('completeDate', 'user',)
        # fields = '__all__' # przekazanie wszystkich pól do formularza
