"""
URL configuration for mysite project.

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
from django.urls import include,path
from users import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('food/',include('food.urls')), #created a seprated url in food attached to this
    path('register/',user_views.register,name='register'), #importing view from user as user_view i.e passed in there
    path("profile/",user_views.profilepage,name='profile'),
    
    #class based view inbuilt
    path("login/",authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path("logout/",authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    
    #function based created from scratch
    #path('login/',user_views.log_in,name='log_in'), mine created below one using frame work
    #path('logout/',user_views.log_out,name='log_out')
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #TO ACESS MEDIA ROOT OF SETTING.PY

"""
urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
"""