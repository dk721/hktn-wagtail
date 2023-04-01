from django.shortcuts import render, redirect
from .forms import BlogPostForm

def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog-post-detail', pk=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})
