from django.shortcuts import render, redirect
from server.apps.posts.models import Post,DevtoolList
from django.http.request import HttpRequest


def site_main(request: HttpRequest, *args, **kwargs):
    posts = Post.objects.all()
    text = request.GET.get("text")
    if text:
        posts = posts.filter(content__contains=text)

    return render(request, "posts/site_main.html", {"posts": posts})


def site_iddetail(request: HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    context ={
        "post":post,
    }
    return render(request, "posts/site_iddetail.html", context=context)


def site_idcreate(request: HttpRequest, *args, **kwargs):
    devtools=DevtoolList.objects.all()
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            interest=request.POST["interest"],
            content=request.POST["content"],
            image=request.FILES["image"]
            devtools=DevtoolList.objects.get(id=devtools_id)
        )
        return redirect("/")
    
    context ={
        "devtools":devtools
    }
    return render(request, "posts/site_idcreate.html",context=context)


def site_iddelete(request: HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")


def site_idupdate(request: HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return redirect(f"/posts/{post.id}")
    return render(request, "posts/site_idupdate.html", {"posts": posts})

def site_devlist(request: HttpRequest, *args, **kwargs):
    posts = Post.objects.all()
    text = request.GET.get("text")
    if text:
        posts = posts.filter(content__contains=text)

    return render(request, "posts/site_devlist.html", {"posts": posts})


def site_devdetail(request: HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    return render(request, "posts/site_devdetail.html", {"post": post})


def site_devcreate(request: HttpRequest, *args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            interest=request.POST["interest"],
            content=request.POST["content"],
        )
        return redirect("/")
    return render(request, "posts/site_devcreate.html")


def site_devdelete(request: HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")


def site_devupdate(request: HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return redirect(f"/posts/{post.id}")
    return render(request, "posts/site_devupdate.html", {"post": post})
