from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import ListCard

class ListCardView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single list card
        """
        try:    
            list_card = ListCard.objects.get(pk=pk)
            serializer = ListCardSerializer(list_card)
            return Response(serializer.data)
        except ListCard.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
 
    def list(self, request):
        """"Handle GET requests for all list cards"""
        list_cards = ListCard.objects.all()

        serializer = ListCardSerializer(list_cards, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized list card instance
        """
        list_card = ListCard.objects.create(
            id=request.data["id"],
            board=request.data["board"],
            user=request.data["user"],
            list_item=request.data["list_item"],
            priority=request.data["priority"]
        )
        serializer = ListCardSerializer(list_card)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a list card

        Returns:
            Response -- Empty body with 204 status code
        """

        list_card = ListCard.objects.get(pk=pk)
        list_card.board = request.data["board"],
        list_card.user = request.data["user"],
        list_card.list_item = request.data["list_item"],
        list_card.priority = request.data["priority"]

        list_card.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all list cards"""
        list_card = ListCard.objects.get(pk=pk)
        list_card.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ListCardSerializer(serializers.ModelSerializer):
    """"JSON serializer for list cards"""
    class Meta:
        model = ListCard
        fields = ('id', 'board', 'user', 'list_iem', 'priority')
