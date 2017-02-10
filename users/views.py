from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
    """Log the user out."""
    # Call logout from within the view function and redirect to home page.
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
    
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display a blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)
        
        # Check that information is valid 
        if form.is_valid():
            # Save username and hash of the password to the database
            # Store created user object in new_user
            new_user = form.save()
            # Log the user in and then redirect to home page.
            # Call authenticate() with username and password as arguments
            # When the user registers they provide two passwords that must match
            # Get either from the forms POST data. Store the authenticated
            # user object.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            # Call login() with request and authenticated_user as args to
            # create session for new user and redirect to home page
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    
    context = {'form':form}
    return render(request, 'users/register.html', context)
