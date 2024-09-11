from django.db import models  # type: ignore

# Create your models here.
#モデルライブりのモデルモジュールをつかう
class Post(models.Model):
# 詳細な属性を定義していく
    # 文字列が入ったCahrFieldというメソッドを使う#オプションは100文字まで。
    title = models.CharField(max_length=100)#modelsライブラリの様々な
# published掲載日に時間の機能を渡す
    published = models.DateTimeField()#modelsライブラリのDatteTimeFieldメソッドをつかう
#データのタイプを宣言している。
    image = models.ImageField(upload_to="media/")#オプションにmedia/というところに画像ファイルをおくよというオプションをする。
 #ImageFieldメソッドつかう
 
 #blog記事に写真という持ちたい情報があったのでimageをもたせる
#/は配下
    body = models.TextField()#本文をもちたい情報として=TexFielsd()メソッド(長文可能なデータ)機能を渡す。

    def __str__(self):#上でself.titleをかえす。
        return self.title 

    #サマリーを返すメソッドを作る。 #先頭にしていた文字だけsumaryをかえす
    def summary(self):
    #    先頭から100文字。
        return self.body[:30]
    



