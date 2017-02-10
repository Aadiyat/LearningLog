"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# This file represents URLS used by the project as a whole. We will need to
# include urls for the learning_logs app in this file.

from django.conf.urls import include, url
from django.contrib import admin


# The body of the file defines urlpatterns variable. 
urlpatterns = [
    # The url patterns variable includes sets of URLS from the apps in the 
    # project. The code includes the module admin.site.urls which defines all
    # the URLs that can be requested from the admin site.
    url(r'^admin/', admin.site.urls),
    # Inlcude the learning_logs.urls modeul. This includes a namespace arg to 
    # distinguish learninglogs' URLs from other URLs that might appear in the
    # project.
    url(r'', include('learning_logs.urls', namespace='learning_logs')),
    # Include urls for users app. This will match urls that start with
    # 'localhost:8000/users/'
    url(r'^users/', include('users.urls', namespace='users')),
]
