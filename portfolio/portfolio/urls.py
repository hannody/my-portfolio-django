"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
# below two imports (settings and static) is to tell this URLS file to import the settings.py file that
#conatins the MEDIA_URL, MEDIA_ROOT and static info...
# then I need to put a + sign after the end bracket of urlpatterns and add the
# link/url to our image folder inside media folder, now, if you press an image from
#the admin page it should show the image that linked with.
from django.conf import settings
from django.conf.urls.static import static
from jobs.views import showJobsPage
#from blog.views import showBlogPage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', showJobsPage, name ='home'),
    path('blog/', include('blog.urls'))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
