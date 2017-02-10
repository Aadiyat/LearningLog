from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Import the model associated with the data we need.
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

# When a URl request matches the pattern defined in urls.py Django will look
# for index() in views.py. Django then passes request object to this function.
# In this case we don'tneed to process any data so the only code is a call to 
# render(). Render has two args, the request object and a template to build the
# page.

# Only registered users should be able to access the login page. 
# A decorator is a directive placed just before a function that Python applies
# to the function to alter its behaviour
# login_required() will check if the user is logged in and only allow access
# to topics() if they are. Else the user will be redirected to the login page.
@login_required
def topics(request):
    """Show all topics."""
    # Query database asking for topics objects sorted by date.
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # Context is a dictionary in which the keys are names used in the template
    # to access the dat and the values are the data that is sent to the 
    # template.
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required    
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    # Accept value of topic id and retrieve the appropriate topic object
    topic = Topic.objects.get(id=topic_id)
    # Make sure topic belongs to user
    if topic.owner != request.user:
        raise Http404
    # Get all the entries associated with this topic, ordered by date in 
    # reverse order.
    entries = topic.entry_set.order_by('-date_added')
    # Send topic and entry to context dictionary.
    context = {'topic': topic,  'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

# new_topic needs to handle two situations - initial requests for the new_topic
# page and then processing any data submitted. It then needs to redirect the 
# user to the topics page.

# Two main type of requests are GET and POST requests. GET is only for reading
# and POST is for submitting information through a form. 
# The browser will intially send a GET request for the page. Once the user 
# submits information the browser will send a POST request if there is valid
# information being submitted.
@login_required
def new_topic(request):
    """Add a new topic."""
    # While the user is on the page determine if request is GET or POST
    if request.method != 'POST':
        # No data submitted; create a blank form that the user can fill out
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            # Need to set owner attribute for a new topic.
            # Call form.save() to return a topic object. Commit=False so that
            # the topic is not yet saved to the database
            new_topic = form.save(commit=False)
            # Set owner to the current user
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required    
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    # use topic_id to get the correct topic.
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # No data submitted. Create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Pass False to commit to create a new entry object without saving
            # to the database.
            new_entry = form.save(commit=False)
            # Set topic to the topic we pulled from the database.
            new_entry.topic = topic
            # Save new_entry once the correct topic has been set.
            new_entry.save()
            # Redirect user to the topic page.
            return HttpResponseRedirect(reverse('learning_logs:topic', 
                                        args=[topic_id]))
    
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    # Get the entry that is to be editted and the topic associated with this
    # entry.
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        # Initial request; 
        # Create a form with instance entry to prefill the form with info from
        # the entry object.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        # pass instance entry again to tell django to create a form with info
        # already existing and any new info.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            # After saving redirect to the page for the topic associated with
            # the entry.
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                        args=[topic.id]))
    
    context = {'entry':entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs\edit_entry.html', context)
    
        
        
