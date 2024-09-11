from django.urls import path # type: ignore
from . import views

#confはいらないのわからない

#urlsは作ったのdjangoはアプリ全体最後の指定先のurlを読み込みなさい
#confはわからない。
from .import views 
#同じ階層から読み込みなさい

#r:正規表現
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("posts/<int:post_id>", views.post_detail, name="post_detail"),#関数post_id
    ]
 

#r'^s&はわかない
#pathに今のバージョンは変わって^やrはいらなくなったそう。
# urlオブジェクトにわたすviews.indexを指定している
# urlオブジェクトにわたすname="index" nameオプションのような物はindexという文字にしてください
