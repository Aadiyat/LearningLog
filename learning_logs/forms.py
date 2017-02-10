# Any page that lets users submit information on a webpage is a form.
# We need to validate information to make sure it's not malicious. Then process
# and save valid information.
# The  simplest way to build a form in Django is to use a ModelForm which uses
# models defined previously to automatically generate a form.

from django import forms

from .models import Topic, Entry


# Define a class called TopicForm that inherits from ModelForm.
class TopicForm(forms.ModelForm):
  # A nested Meta class tells Django which model to base the form on and which
  # fields to include
    class Meta:
        model = Topic
        fields = ['text']
        # Let Django generate a label for the text field.
        labels = {'text': ''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # Widgets are HTML form elemtns such as single line text boxes.
        # Set width of text field to 80 columns.
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
