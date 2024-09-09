import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from.models import Post #モデル.pyのpythonのファイルから
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FoursquareSearchView(APIView):
    def get(self, request):
        # Foursquare APIキーとエンドポイント
        api_key = 'YOUR_FOURSQUARE_API_KEY'
        endpoint = 'https://api.foursquare.com/v2/venues/search'
        params = {
            'll': request.query_params.get('ll', '40.7,-74'),  # デフォルトの位置
            'query': request.query_params.get('query', 'restaurant'),
            'client_id': api_key,
            'client_secret': 'YOUR_FOURSQUARE_CLIENT_SECRET',
            'v': '20230901'  # APIのバージョン
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({'error': 'Failed to fetch data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GoogleMapsGeocodeView(APIView):
    def get(self, request):
        # Google Maps APIキーとエンドポイント
        api_key = 'AIzaSyBU75_X63j5lg_VgMAvFZonpbp1_reDtE0'
        endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {
            'address': request.query_params.get('address', '1600+Amphitheatre+Parkway,+Mountain+View,+CA'),
            'key': api_key
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({'error': 'Failed to fetch data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
