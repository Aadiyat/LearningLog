"""Define URL pattersn for users"""

from django.conf.urls import url
# import the default django login view
from django.contrib.auth.views import login

from .import views

urlpatterns = [
    # Login page. The urlpattern will match localhost:8000/users/login/
    # The view argument is the default django login view
    # Also pass a dictionary to the template location
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    # Logout page
    url(r'^logout/$', views.logout_view, name='logout'),
    # user registration page. Pattern matches 'localhost:8000/users/register'
    url(r'^register/$', views.register, name='register'),
]
