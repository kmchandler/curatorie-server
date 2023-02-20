from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import SharedBoard, User, Board

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

        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            shared_boards = shared_boards.filter(user_id=user_id)

        serializer = SharedBoardSerializer(shared_boards, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations, Returns Response -- JSON serialized shared board instance"""

        user = User.objects.get(id=request.data["user_id"])

        board = Board.objects.get(id=request.data["board_id"])

        shared_board = SharedBoard.objects.create(
            user = user,
            board = board
        )
        serializer = SharedBoardSerializer(shared_board)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a shared board, Returns Response -- Empty body with 204 status code"""

        user = User.objects.get(id=request.data["user_id"])

        board = Board.objects.get(id=request.data["board_id"])

        shared_board = SharedBoard.objects.get(pk=pk)
        shared_board.user = user
        shared_board.board = board

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
