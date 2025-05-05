from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/list.html', {'blogs': blogs})

@login_required
def blog_write(request):
    try:
        if request.method == 'POST':
            form = BlogPostForm(request.POST)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.author = request.user
                blog_post.save()
                messages.success(request, '博客发布成功！')
                return redirect('blog:list')
            else:
                messages.error(request, '表单验证失败，请检查输入。')
        else:
            form = BlogPostForm()
        
        return render(request, 'blog/write.html', {'form': form})
    except Exception as e:
        messages.error(request, f'发生错误：{str(e)}')
        return redirect('blog:list')
