"""Each user will need to create a number of topics in their learning logs.
Each entry will be tied to a topic, and displayed as text. Each entry will also
require a timestamp."""

# Import models module
from django.db import models
from django.contrib.auth.models import User
# Create your models here. A model tells Django how to work with the data that 
# will be stored in the app.

# Create a class Topic that inherits from Model
class Topic(models.Model):
    """A topic the user is learning about."""
    # Text attribute is a Character Field. CharFields store small amounts of 
    # text. 
    text = models.CharField(max_length=200)
    # Date_added will record a date and time. Auto_now_add enabled so Django 
    # will automatically set date and time to current date and time.
    date_added = models.DateTimeField(auto_now_add=True)
    # Add a foreign key relationship to determine which topic belongs to which
    # user.
    owner = models.ForeignKey(User)
    # Need to determine which attribute to use by default when displaying info
    # about a topic. 
    # Django calls __str__ method to display a simple representation of the 
    # model. 
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
        
# Many entries can be made about one topic.
class Entry(models.Model):
    """Something specific learned about a topic."""
    # First attribute is an instance of  ForeignKey. A ForeignKey is a reference
    # to another record in the database.  Each topic is assigned a key when it
    # is created. Django uses the key associated with each piece of information
    # to establish a connection between two pieces of data. This connection is
    # used to retrieve all the entries associated with a certain topic.
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    # Meta class is nested inside Entry. Meta holds extra info for managing a 
    # model. Set a special attribute to tell Dhango to use 'Entries' when 
    # refering to multiple entries. Otherwise Django would refer to multiple
    # entries as 'Entrys'
    class Meta:
        verbose_name_plural = 'entries'
    
    # Define what to use when Django refers to individual entires.    
    def __str__(self):
        """Return a string representation of the model."""
        # Since text fields can be very large show the first 50 characters of 
        # each entry.
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + '...'
        
