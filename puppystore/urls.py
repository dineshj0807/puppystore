"""puppystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from puppy.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/v1/puppies/(?P<pk>[0-9]+)/$',
        get_delete_update_puppy, name='get_delete_update_puppy'),
    re_path(r'^api/v1/puppies/$', get_post_puppies, name='get_post_puppies'),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='Token_Obtain_Pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='Token_Refresh_View'),
]
