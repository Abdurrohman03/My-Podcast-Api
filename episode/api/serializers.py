from profile.api.serializers import ProfileSerializer
from profile.models import Profile
from ..models import Tag, Category, Season, Podcast, Comment, Like, PlaylistSingle, PlaylistBase
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'title', 'season_id']


class PodcastGETSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    author = ProfileSerializer(read_only=True)
    season = SeasonSerializer(read_only=True)

    class Meta:
        model = Podcast
        fields = ['id', 'title', 'image', 'author', 'audio_file', 'category', 'tags', 'description', 'created_date',
                  'views', 'season']


class PodcastPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['id', 'title', 'image', 'author', 'audio_file', 'category', 'tags', 'description', 'created_date',
                  'views', 'season']
        extra_kwargs = {
            'author': {'required': False}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance



class ComentGETSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.user.username')
    article = serializers.CharField(source='article.title', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date', 'name']


class ComentPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date', 'name']
        extra_kwargs = {
            'author': {'required': False},
            'article': {'required': False},
            'name': {'required': False},
        }

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        episode_id = self.context.get('episode_id')
        description = validated_data.get('description')
        name = validated_data.get('name')
        instance = Comment.objects.create(author=author, article_id=episode_id, description=description, name=name)
        return instance


class LikeGETSerializer(serializers.ModelSerializer):
    music = PodcastGETSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['music']


class LikePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'author', 'music']
        extra_kwargs = {
            'author': {'required': False},
            'music': {'required': False},
        }

    def create(self, validated_data):
        request = self.context.get('request')
        music_id = self.context.get('music_id')
        author_id = request.user.profile.id
        instance = Like.objects.create(author_id=author_id, music_id=music_id)
        return instance



class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistBase
        fields = '__all__'


class PlaylistSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistSingle
        fields = '__all__'
