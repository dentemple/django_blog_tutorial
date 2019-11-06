# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# posts = [
#     {
#         "author": "Kurtz",
#         "title": "Blog Post 1",
#         "content": "First post content",
#         "date_posted": "Yesterday",
#     },
#     {
#         "author": "Marlow",
#         "title": "Blog Post 2",
#         "content": "First post content",
#         "date_posted": "Today",
#     },
# ]


def home(request):
    # return HttpResponse("<h1>Blog Home</h1>")
    # context = {"posts": posts}
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about(request):
    # return HttpResponse("<h1>Blog About</h1>")
    return render(request, "blog/about.html", {"title": "About"})
