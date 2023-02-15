from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import InspoCard, User, Board

class InspoCardView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single inspo card
        """
        try:    
            inspo_card = InspoCard.objects.get(pk=pk)
            serializer = InspoCardSerializer(inspo_card)
            return Response(serializer.data)
        except InspoCard.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
 
    def list(self, request):
        """"Handle GET requests for all inspo cards"""
        inspo_cards = InspoCard.objects.all()

        board_id = request.query_params.get('board_id', None)
        if board_id is not None:
            inspo_cards = inspo_cards.filter(board_id=board_id)

        serializer = InspoCardSerializer(inspo_cards, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized inspo card instance
        """

        user = User.objects.get(id=request.data["user_id"])

        board = Board.objects.get(id=request.data["board_id"])

        inspo_card = InspoCard.objects.create(
            board=board,
            user=user,
            image_url=request.data["image_url"],
            description=request.data["description"],
            priority=request.data.get("priority", False)
        )
        serializer = InspoCardSerializer(inspo_card)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for an inspo card

        Returns:
            Response -- Empty body with 204 status code
        """

        user = User.objects.get(id=request.data["user_id"])

        board = Board.objects.get(id=request.data["board_id"])

        inspo_card = InspoCard.objects.get(pk=pk)
        inspo_card.board = board
        inspo_card.user = user
        inspo_card.image_url = request.data["image_url"]
        inspo_card.description = request.data["description"]
        inspo_card.priority = request.data["priority"]

        inspo_card.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all inspo cards"""
        inspo_card = InspoCard.objects.get(pk=pk)
        inspo_card.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class InspoCardSerializer(serializers.ModelSerializer):
    """"JSON serializer for inspo cards"""
    class Meta:
        model = InspoCard
        fields = ('id', 'board', 'user', 'image_url', 'description', 'priority')
