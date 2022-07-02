from django.shortcuts import render
from django.utils import timezone
from .models import Post

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