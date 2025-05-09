from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
import base64
from django.core.files.base import ContentFile
from posts.models import Comment, Post, Group, User, Follow


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'posts'
        )
        ref_name = 'ReadOnlyUsers'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id',
            'title',
            'slug',
            'description'
        )


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        read_only_fields = ('author', 'pub_date')

    def validate_text(self, value):
        if not value:
            raise serializers.ValidationError({
                'text': 'Текст публикации не может быть пустым'
            })
        return value

    def validate_group(self, value):
        if value is not None:
            if isinstance(value, Group):
                return value.id
            try:
                Group.objects.get(id=value)
                return value
            except Group.DoesNotExist:
                raise serializers.ValidationError(
                    {"group": "Указанной группы не существует"}
                    )
        return value

    def create(self, validated_data):
        if 'group' in validated_data and validated_data['group'] is not None:
            group_id = validated_data['group']
            try:
                group = Group.objects.get(id=group_id)
                validated_data['group'] = group
            except Group.DoesNotExist:
                raise serializers.ValidationError(
                    {"group": "Specified group does not exist"}
                    )
        return Post.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'text',
            'created',
            'author'
        )
        read_only_fields = (
            'author',
            'post',
            'created'
        )


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Вы уже подписаны на этого автора'
            )
        ]

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return value
