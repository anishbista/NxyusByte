from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})


def post_detail(request, pk):
    posts = Post.objects.prefetch_related("comment").get(pk=pk)
    return render(request, "post_detail.html", {"posts": posts})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect("post_list")
    else:
        form = PostForm()

    return render(request, "create_post.html", {"form": form})
