from django.urls import path, include
from . import views
#from . import views

urlpatterns = [
    path('', views.showBlogPage, name='all_blogs'),
    path('<int:blog_id>/', views.detailPages, name='detail'),
]
