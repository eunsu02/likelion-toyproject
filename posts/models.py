from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True

class Post(BaseModel):
    post_id=models.AutoField(primary_key=True)
    content=models.TextField(verbose_name="내용",null=True, blank=True)
    name=models.CharField(verbose_name="작성자",max_length=20,null=True, blank=True)