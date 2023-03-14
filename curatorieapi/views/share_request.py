from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.db import IntegrityError
from curatorieapi.models import ShareRequest, User, Board

class ShareRequestView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single share request"""
        try:
            share_request = ShareRequest.objects.get(pk=pk)
            serializer = ShareRequestSerializer(share_request)
            return Response(serializer.data)
        except ShareRequest.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
            status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all share requests"""
        share_requests = ShareRequest.objects.all()
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            share_requests = share_requests.filter(user_id=user_id)

        serializer = ShareRequestSerializer(share_requests, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations, Returns Response -- JSON serialized share request instance"""

        user = User.objects.get(id=request.data["user_id"])
        board = Board.objects.get(id=request.data["board_id"])

        try: 
            share_requests = ShareRequest.objects.create(
                user = user,
                board = board
            )
            serializer = ShareRequestSerializer(share_requests)
            return Response(serializer.data)
        except IntegrityError:
            return Response({'message': 'cannot send duplicate boards to the same user'},
            status=status.HTTP_409_CONFLICT)

    def update(self, request, pk):
        """Handle PUT requests for a share request, Returns Response -- Empty body with 204 status code"""

        user = User.objects.get(id=request.data["user_id"])

        board = Board.objects.get(id=request.data["board_id"])

        share_request = ShareRequest.objects.get(pk=pk)
        share_request.user = user
        share_request.board = board

        share_request.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """Handle delete requests for all share requests"""
        share_request = ShareRequest.objects.get(pk=pk)
        share_request.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ShareRequestSerializer(serializers.ModelSerializer):
    """JSON serializer for share requests"""
    class Meta:
        model = ShareRequest
        fields = ('id', 'user', 'board')
