from django.contrib import admin # type: ignore

# Register your models here.
from . models import Post


admin.site.register(Post)#adminライブラリのsiteモジュールをつかって管理サイトにするの#.registerメソッド使用。Post機能