import requests
from django.shortcuts import render, get_object_or_404 # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Post  # モデルをインポート

def index(request):
    # return HttpResponse("Hello World!")
    posts = Post.objects.order_by('-published') #Post.objects取り出した全てのデータ全てのオブジェクトをもってくる。
    
#    oder_by()メソッドで-published公開日の降順でソートする持たせる
#    ソート: 並び替えること

    return render(request, 'posts/index.html/',  {'posts': posts})#直接returnするのではなくて外部のhtmlのほうを読みこんでブラウザにもどしてあげる。
# Create your views here.
#indexと呼ばれたページの内容をレンダリングしているこれを
# レンダリングする前にPostから取り出した値をテンプレートに添えて転送
# してあげる

#post_idの辞書をつくりそれをposts /detail_htmlに渡す render関数でファイルの情報をファイル間で転送。
#posts/post_detailのapplication
def post_detail(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    #postにPostクラスの.objects getメソッドでそのインデックス番号をそれぞれ取得した物をpostに持たせる
    return render(request, 'posts/post_detail.html', {'post': post})#postの情報をキーに渡してからrender→posts/post_detail.html'に転送する。
#postsの下にposts_ihtmlというファイルを作ってpostの情報を渡す
# 'post_id':post_idに渡すという操作がわからない
#Postクラスのインスタンにデータを渡す。辞書のキーにつかう。データを転送

def about(request):
    return render(request, 'posts/about.html')
