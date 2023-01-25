import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Post

def main(request):
    posts = Post.objects.all()
    context ={
        'posts': posts,
    }
    return render(request, "posts/main.html", context=context)
    
    
@csrf_exempt
def like_ajax(requset):
    req = json.loads(requset.body)
    post_id = req['id']
    button_type = req['type']
    post = Post.objects.get(id=post_id)
    
    if button_type == 'like':
        post.status = True
        post.save()
        return JsonResponse({'id': post_id, 'type': button_type})
    
    else:
        post.status = False
        post.save()
        return JsonResponse({'id': post_id, 'type': button_type})
        

