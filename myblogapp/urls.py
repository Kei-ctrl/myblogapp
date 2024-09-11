from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from posts import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("posts/", include("posts.urls")),
    path("admin/", admin.site.urls),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail")  # 修正: URLパターンにスラッシュを追加
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
