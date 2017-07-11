from rest_framework import serializers

from ..models import Post

__all__ = (
    'PostSerializer',
)

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ('pk', 'photo',)
