from rest_framework import serializers
from .models import Author, Article


class AuthorSerializer(serializers.ModelSerializer):
    """
    Author Serializers
    """
    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    """
    Article Serializer for Admin and Logged in users.
    """
    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['author'] = AuthorSerializer(read_only=True)
        return super().to_representation(instance)


class ArticleListSerializer(serializers.ModelSerializer):
    """
    Article Serializer for list action
    """
    class Meta:
        model = Article
        exclude = ['firstParagraph', 'body']

    def to_representation(self, instance):
        self.fields['author'] = AuthorSerializer(read_only=True)
        return super().to_representation(instance)


class AnonymousArticleSerializer(serializers.ModelSerializer):
    """
    Article Serializer for Anonymous users.
    """
    class Meta:
        model = Article
        exclude = ['body']

    def to_representation(self, instance):
        self.fields['author'] = AuthorSerializer(read_only=True)
        return super().to_representation(instance)
