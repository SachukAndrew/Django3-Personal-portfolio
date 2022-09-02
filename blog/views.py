from django.shortcuts import render

from . import Message

def all_blogs(request):
    blogs = Message.objects.all()
    return render(request, 'blog/all_blogs.html', {"blogs": blogs})
