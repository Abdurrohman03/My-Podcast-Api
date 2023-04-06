from ..models import Blog, CommentBlog
from rest_framework import serializers
from profile.api.serializers import ProfileSerializer
from episode.api.serializers import TagSerializer, CategorySerializer


class BlogGETSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'image', 'author', 'description', 'created_date', 'views', 'tags', 'category']


class BlogPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'author', 'description', 'created_date', 'views', 'tags', 'category']
        # extra_kwargs = {
        #     'author': {'required': False},
        #     'views': {'required': False},
        #     'image': {'required': False},
        # }

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class MiniBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'created_date']


class CommentGETSerializer(serializers.ModelSerializer):
    article = MiniBlogSerializer(read_only=True)
    author = ProfileSerializer(read_only=True)

    class Meta:
        model = CommentBlog
        fields = ['id', 'author', 'article', 'description', 'created_date', 'name']


class CommentPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentBlog
        fields = ['id', 'author', 'article', 'description', 'created_date', 'name']
        extra_kwargs = {
            'article': {'required': False}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        author = None
        if request.user.is_authenticated:
            author = request.user.profile
        article_id = self.context.get('article_id')
        instance = super().create(validated_data)
        instance.author = author
        instance.article_id = article_id
        instance.save()
        return instance
