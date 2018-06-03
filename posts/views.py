from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):

    #Postオブジェクトを取得
    posts =  Post.objects.order_by('pub_date')

    #home.htmlにはディクショナリ形式の引数を与えることでデータを渡すことができる！
    return render(request, 'posts/home.html',{'posts':posts})
