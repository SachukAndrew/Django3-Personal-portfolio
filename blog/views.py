from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect

from .models import Message

def all_blogs(request):
    # blog_count = Message.objects.count() - так можно создать переменную для подсчета постов
    blogs = Message.objects.order_by('-date')[0:5]
    return render(request, 'blog/all_blogs.html', {"blogs": blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Message, pk=blog_id)
    return render(request, 'blog/detail.html', {"blog": blog})

def Linkedin(request):
    return HttpResponseRedirect('https://www.linkedin.com/in/andrey-sachuk/')
