from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import Board, User

class BoardView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single board
        """
        try:    
            board = Board.objects.get(pk=pk)
            serializer = BoardSerializer(board)
            return Response(serializer.data)
        except Board.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """"Handle GET requests for all boards"""
        boards = Board.objects.all()

        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            boards = boards.filter(user_id=user_id)

        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized board instance
        """
        user = User.objects.get(id=request.data["user_id"])
        
        board = Board.objects.create(
            user=user,
            name=request.data["name"],
            icon=request.data["icon"]
        )
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a board

        Returns:
            Response -- Empty body with 204 status code
        """

        user = User.objects.get(id=request.data["user_id"])

        board = Board.objects.get(pk=pk)
        board.user = user
        board.name = request.data["name"]
        board.icon = request.data["icon"]

        board.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all boards"""
        board = Board.objects.get(pk=pk)
        board.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class BoardSerializer(serializers.ModelSerializer):
    """"JSON serializer for boards"""
    class Meta:
        model = Board
        fields = ('id', 'user_id', 'name', 'icon')
