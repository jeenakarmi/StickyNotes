"""
URL configuration for Notes_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import HomeView  # Importing HomeView from the home app views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),  #authorized\
    path('', HomeView.as_view(), name='home'),  # Mapping root URL to the HomeView class
    path('smart/',include('notes.urls')) #path -- naming smart for notes's urls   # Including URLs from the 'notes' app under 'smart/'
]


