from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser

from .models import Article, Author
from .serializers import (ArticleSerializer, ArticleListSerializer,
                          AnonymousArticleSerializer, AuthorSerializer)


class AdminAuthorViewSet(viewsets.ModelViewSet):
    """
    View endpoint for Author CRUD
    Obs: Exclusive for Admin users
    """
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAdminUser]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AdminArticleViewSet(viewsets.ModelViewSet):
    """
    View endpoint for Article CRUD
    Obs: Exclusive for Admin users
    """
    permission_classes = [IsAdminUser]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleViewSet(viewsets.GenericViewSet, ListModelMixin,
                     RetrieveModelMixin):

    def get_serializer_class(self):
        """
        Selects the serializer class depending on action and authentication
        """
        if self.action == 'retrieve':
            user = self.request.user
            if user.is_authenticated:
                return ArticleSerializer
            return AnonymousArticleSerializer
        else:
            return ArticleListSerializer

    def get_queryset(self):
        """
        Filter queryset depending on the request query params
        category and author name.
        """
        queryset = Article.objects.all().select_related('author')
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category=category)
        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author__name__exact=author)
        return queryset
