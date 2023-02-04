from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import SharedBoard

class SharedBoardView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single shared board"""
        try:
            shared_board = SharedBoard.objects.get(pk=pk)
            serializer = SharedBoardSerializer(shared_board)
            return Response(serializer.data)
        except SharedBoard.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
            status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all shared boards"""
        shared_boards = SharedBoard.objects.all()

        serializer = SharedBoardSerializer(shared_boards, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations, Returns Response -- JSON serialized shared board instance"""

        shared_board = SharedBoard.objects.create(
            id=request.data["id"],
            user = request.data["user"],
            board = request.data["board"]
        )
        serializer = SharedBoardSerializer(shared_board)
        return Response(serializer.data)

    def updated(self, request, pk):
        """Handle PUT requests for a shared board, Returns Response -- Empty body with 204 status code"""

        shared_board = SharedBoard.objects.get(pk=pk)
        shared_board.user = request.data["board"],
        shared_board.board = request.data["user"]

        shared_board.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """Handle delete requests for all shared boards"""
        shared_board = SharedBoard.objects.get(pk=pk)
        shared_board.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SharedBoardSerializer(serializers.ModelSerializer):
    """JSON serializer for shared boards"""
    class Meta:
        model = SharedBoard
        fields = ('id', 'user', 'board')
