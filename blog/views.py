from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

'''
views connect models and templates. In our post_list view we will need to take the models we want to display and pass them to the template. 
'''

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #posts = name of QuerySet
    return render(request, 'blog/post_list.html', {'posts': posts})

'''
To display our QuerySet on our blog's post list, we have two things left to do:

Pass the posts QuerySet to the template context, by changing the render function call. We'll do this now.
Modify the template to display the posts QuerySet. We'll cover this in a later chapter.

In the render function we have one parameter request (everything we receive from the user via the Internet)
and another giving the template file ('blog/post_list.html'). The last parameter, {}, is a place in which we can add some things for the template to use.
We need to give them names (we will stick to 'posts' right now). :)
It should look like this: {'posts': posts}. Please note that the part before : is a string; you need to wrap it with quotes: ''.

'''

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post}) # to extend application - post view

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})