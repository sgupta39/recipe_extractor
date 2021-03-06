"""recipe_extractor URL Configuration

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
#from django.conf.urls import *
from django.urls  import path, include
# from django.conf.urls import reverse
from register.views import (
    User_View, user_login,logout
)
from userhomepage.views import (
    user_homepage, WriteRecipeApiView, GetRecipeView, UploadLinkApiView
)


urlpatterns = [

    # path('recipe/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('register/', include("register.urls") ),
    path('', user_login, name ="login" ),
    path('userhomepage/', user_homepage, name ="userhomepage" ),
    path('',logout, name ="logout" ),
    path('write_recipe/', WriteRecipeApiView.as_view(), name  ='writeRecipe'),
    path('', WriteRecipeApiView.as_view(), name  ='postRecipe'),
    #path('get_Recipe/', get_Recipe, name='getRecipe'),
    path('get_Recipe/', GetRecipeView.as_view(), name='getRecipe'),
    path('', GetRecipeView.as_view(), name  ='updateRecipe'),
    path('upload_link/', UploadLinkApiView.as_view(), name  ='upload_link'),
    path('userhomepage/',user_homepage,name="searchRecipe"),

]

 