"""
URL configuration for petcare project.

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
# project_name/urls.py

from django.contrib import admin
from django.urls import path, include  # `include` is used to include app-level URLs

urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),  # Directs to the Django admin site
    
    # Include the URLs from the 'pets' app
    path('', include('pets.urls')),  # Includes routes from the 'pets' app
    
    # Include other apps' URLs here as needed
    # path('other_app/', include('other_app.urls')),  # Example of another app's URLs
]
