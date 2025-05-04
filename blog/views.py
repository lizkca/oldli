from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/list.html', {'blogs': blogs})

@login_required
def blog_write(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog:list')
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/write.html', {'form': form})
