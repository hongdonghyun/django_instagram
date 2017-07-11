from rest_framework import generics
from rest_framework import request
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Post, Comment
from ..serializers import PostSerializer

__all__ = (
    'PostListCreateView',
    'PostLikeToggleVIew',
)


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        instance = serializer.save(author=request.user)
        comment_content = request.data.get('comment')
        if comment_content:
            instance.my_comment = Comment.objects.create(
                post=instance,
                author=request.author,
                content=comment_content,
            )
            instance.save()


class PostLikeToggleVIew(APIView):
    def post(self, request, post_pk):
        post_instance = Post.objects.get(pk=post_pk)
        get_object_or_404(Post, pk=post_pk)
        post_like, post_like_created = post_instance.postlike_set.get_or_create(
            user=request.user,
        )
        if not post_like_created:
            post_like.delete()
        return Response({'created': post_like_created})
