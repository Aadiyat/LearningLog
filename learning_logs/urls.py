"""Defines URL patterns for learning_logs."""

# Import the url function which is needed to map URLs to views
from django.conf.urls import url
# Import views module. The '.' means that views is imported from the same 
# directory as this file.
from . import views

# The urlpatterns in this module is a list of individual pages that can be 
#  requested from the learning_logs app
urlpatterns = [
    # Home page
    # The actual URL pattern is a call to the url function which takes 3 args
    # The first is a regular expression. The r tells Python to interpret the
    # following as a raw string. ^ tells Python to find the beginning of the
    # string, and $ tells Python to look for the end of the string. In its 
    # entirety, the url pattern looks for a URL with nothing between the 
    # beginning and end of an URL.
    url(r'^$', views.index, name='index'),
    # Python ignores the baes URL for the project (http://localhost:8000/) so
    # an empty regular expression matches the base URL. Any other URL will give
    # an error page.
    # The second arg specifies which view function to call. The third arg 
    # gives the name 'index' for this URL pattern so we can refer to it in other
    # sections of the code.
    
    # Basically, the home page is named 'index', there is a function in the 
    # views.py file called index, referring to this home page. That function
    # tells django how to build the page.
    
    # Show all topics.
    # Added topics/ into the regualr expression arguemnt used for the home page
    # This pattern will match any URL that has the base URL followed by topics.
    url(r'^topics/$', views.topics, name='topics'),
    
    # Detailed page for a single topic
    # This will be different since it will use the topics' id to indicate which
    # topic was requested
    # The second part of the regular expression matches an intenger between 
    # two forward slashes and stores the integer value as topic_id. 
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    
    # Page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    
    # Page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    
    # Page for editting an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name='edit_entry'),
]
