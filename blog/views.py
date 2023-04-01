from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

@login_required
def blog_participate(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.participants.add(request.user)
    return redirect('blog_participate', blog_id=blog_id)

@login_required
def blog_participants(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    participants = blog.participants.all()
    return render(request, "blog_participants.html", {'blog': blog, 'participants': participants})


@login_required
def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        user = request.user
        if user in blog.participants.all():
            blog.participants.remove(user)
        else:
            blog.participants.add(user)
        return redirect('blog_detail', pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


def my_blogs(request):
    blog_posts = BlogPost.objects.filter(author=request.user)
    participants = {}
    for blog in blog_posts:
        participants[blog.id] = blog.participants.all()
    return render(request, 'my_blogs.html', {'blog_posts': blog_posts, 'blog_participants': participants})


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
