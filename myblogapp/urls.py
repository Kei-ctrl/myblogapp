import os
from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from posts import views
from rest_framework.routers import DefaultRouter # type: ignore
from posts.views import AttractionViewSet

router = DefaultRouter()
router.register(r'attractions', AttractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("posts/", include("posts.urls")),
    path('api/', include(router.urls)),  # REST API のルーティング
    path("tinder_cards/", views.tinder_cards, name="tinder_cards"),
    path("admin/", admin.site.urls),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),  # 修正: URLパターンにスラッシュを追加
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




