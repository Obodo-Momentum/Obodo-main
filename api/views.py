from rest_framework import viewsets, views
from rest_framework.response import Response
from obodo.models import Comment, RequestOfferPost
from users.models import User
from api.serializers import CommentSerializer
from rest_framework.decorators import action
from django.shortcuts import render, get_object_or_404


class PostCommentsView(views.APIView):
    
    def get(self, request, post_pk, format=None):
        post = get_object_or_404(RequestOfferPost, pk=post_pk)
        serializer = CommentSerializer(post.comments.all(), many=True, context = {'request': request})
        return Response(serializer.data)

    def post(self, request, post_pk, format=None):
        serializer = CommentSerializer(data=request.data)
        post = get_object_or_404(RequestOfferPost, pk=post_pk)
        if serializer.is_valid():
            serializer.save(original_post = post, commenter = request.user, comment_text= request.data)
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(status=400)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
