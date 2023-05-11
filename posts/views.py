from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import  *
from django.db import models
import json

#방명록 삭제
@require_http_methods(["DELETE"])
def delete_post(request,id):
    delete_post=get_object_or_404(Post,pk=id)
    delete_post.delete()
    
    return JsonResponse({
        'status':200,
        'message':'방명록 삭제 성공',
    })


#방명록 조회
@require_http_methods(["GET"])
def get_all(request):
    posts=Post.objects.all()
    category_list=[]
    
    for post in posts:
        category_list.append({
            "id":post.post_id,
            "writer":post.name,
            "content":post.content,
        })
        
    return JsonResponse({
        'status':200,
        'message':'모든 방명록 조회 성공',
        'data':category_list
    })
    
#방명록 생성
@require_http_methods(["POST"])
def create_post(request):
    body=json.loads(request.body.decode('utf-8'))
    
    new_post=Post.objects.create(
        name=body['name'],
        content=body['content']
    )
    
    new_post_json={
        "id":new_post.post_id,
        "name":new_post.name,
        "content":new_post.content
    }
    
    return JsonResponse({
        'status':200,
        'message':'방명록 생성 성공',
        'data':new_post_json
    })