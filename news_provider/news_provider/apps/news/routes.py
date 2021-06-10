from django.urls import include, path
from rest_framework import routers

from .views import AdminArticleViewSet, AdminAuthorViewSet, ArticleViewSet

admin_router = routers.DefaultRouter()
admin_router.register('articles', AdminArticleViewSet,
                      basename='admin_articles')
admin_router.register('authors', AdminAuthorViewSet, basename='admin_authors')

article_router = routers.DefaultRouter()
article_router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('', include(article_router.urls)),
    path('admin/', include(admin_router.urls))
]
