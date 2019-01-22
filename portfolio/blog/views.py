from django.shortcuts import render, get_object_or_404
from .models import Blog

def showBlogPage(request):
    blog_objects = Blog.objects
    #blogs 'blogs' is the key that will be used as blogs.all in the for loop
    # from the html file
    return render(request, 'blog/blog.html',{'blogs_key':blog_objects})

def detailPages(request, blog_id):#blog_id need to be used in the URLS.py in the path
    #get_object_or_404(Class Name, PrimaryKey pk)
    print(blog_id)
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detail_blog})
