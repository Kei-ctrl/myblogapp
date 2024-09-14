from django.urls import path, include # type: ignore
from .views import AttractionViewSet
from rest_framework.routers import DefaultRouter # type: ignore
from .import views 


#confはいらないのわからない

#urlsは作ったのdjangoはアプリ全体最後の指定先のurlを読み込みなさい
#confはわからない。

#同じ階層から読み込みなさい


router = DefaultRouter()
router.register(r"attractions", AttractionViewSet, basename="attractions")

#r:正規表現
urlpatterns = [
    path("", views.index, name="index"), # type: ignore
#    path("about/", views.about, name="about"), # type: ignore
    path("api/", include(router.urls)), 
    path("posts/<int:post_id>", views.post_detail, name="post_detail"),#関数post_id # type: ignore
    path("tinder_cards/", views.tinder_cards, name="tinder_cards"),
]






#r'^s&はわかない
#pathに今のバージョンは変わって^やrはいらなくなったそう。
# urlオブジェクトにわたすviews.indexを指定している
# urlオブジェクトにわたすname="index" nameオプションのような物はindexという文字にしてください




