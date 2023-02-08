from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import BoardType

class BoardTypeView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single board type
        """
        try:    
            board_type = BoardType.objects.get(pk=pk)
            serializer = BoardTypeSerializer(board_type)
            return Response(serializer.data)
        except BoardType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
 
    def list(self, request):
        """"Handle GET requests for all list board types"""
        board_types = BoardType.objects.all()

        serializer = BoardTypeSerializer(board_types, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized board type instance
        """

        board_type = BoardType.objects.create(
            type=request.data["type"]
        )
        serializer = BoardTypeSerializer(board_type)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a board type

        Returns:
            Response -- Empty body with 204 status code
        """

        board_type = BoardType.objects.get(pk=pk)
        board_type.type = request.data["type"]

        board_type.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all board types"""
        board_type = BoardType.objects.get(pk=pk)
        board_type.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class BoardTypeSerializer(serializers.ModelSerializer):
    """"JSON serializer for board types"""
    class Meta:
        model = BoardType
        fields = ('id', 'type')
