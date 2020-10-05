from django.shortcuts import render
from .models import Post
from django.utils import timezone


def blog(request):
    blogpost = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    return render(request, "blog.html", {'blogpost': blogpost})
