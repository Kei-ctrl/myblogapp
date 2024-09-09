from django.contrib import admin

# Register your models here.
from . models import Post


admin.site.register(Post)#adminライブラリのsiteモジュールをつかって管理サイトにするの#.registerメソッド使用。Post機能