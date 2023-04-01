from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

def create_blog_post(request):
    if request.method == "post":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog-post', pk=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})
