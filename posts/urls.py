from django.urls import path
from .views import FoursquareSearchView
#confはいらないのわからない

#urlsは作ったのdjangoはアプリ全体最後の指定先のurlを読み込みなさい
#confはわからない。
from .import views 
#同じ階層から読み込みなさい

#r:正規表現
urlpatterns = [
    path('', views.index, name="index"),
    path('foursquare-search/', FoursquareSearchView.as_view(), name='foursquare-search'),
    path('google-maps-geocode/', GoogleMapsGeocodeView.as_view(), name='google-maps-geocode'),
    ]
 

#r'^s&はわかない
#pathに今のバージョンは変わって^やrはいらなくなったそう。
# urlオブジェクトにわたすviews.indexを指定している
# urlオブジェクトにわたすname="index" nameオプションのような物はindexという文字にしてください
