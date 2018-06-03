from django.db import models

# Create your models here.

class Post(models.Model):
    '''
    記事の内容を管理するクラスと思われる。  

    modelの定義はここに詳しく書いてある。
    https://docs.djangoproject.com/ja/1.11/ref/models/fields/
    '''
    #タイトル
    title = models.CharField(max_length=250)
    #発行日
    pub_date = models.DateTimeField()
    #適当な画像
    image = models.ImageField(upload_to='media/')
    #記事本文
    body = models.TextField()
