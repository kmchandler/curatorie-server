from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import GiftCard, User, Board

class GiftCardView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single gift card
        """
        try:    
            gift_card = GiftCard.objects.get(pk=pk)
            serializer = GiftCardSerializer(gift_card)
            return Response(serializer.data)
        except GiftCard.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
 
    def list(self, request):
        """"Handle GET requests for all gift cards"""
        gift_cards = GiftCard.objects.all()

        board_id = request.query_params.get('board_id', None)
        if board_id is not None:
            gift_cards = gift_cards.filter(board=board_id)

        serializer = GiftCardSerializer(gift_cards, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized gift card instance
        """
        user = User.objects.get(id=request.data["user_id"])

        board = Board.objects.get(id=request.data["board_id"])

        gift_card = GiftCard.objects.create(
            board=board,
            user=user,
            link=request.data["link"],
            image_url=request.data["image_url"],
            item=request.data["item"],
            description=request.data["description"],
            price=request.data["price"],
            occasion=request.data["occasion"],
            gift_for=request.data["gift_for"],
            name=request.data["name"],
            priority=request.data["priority"]
        )
        serializer = GiftCardSerializer(gift_card)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a gift card

        Returns:
            Response -- Empty body with 204 status code
        """
        user = User.objects.get(id=request.data["user_id"])

        board = Board.objects.get(id=request.data["board_id"])

        gift_card = GiftCard.objects.get(pk=pk)
        gift_card.board = board
        gift_card.user = user
        gift_card.link = request.data["link"]
        gift_card.image_url = request.data["image_url"]
        gift_card.item = request.data["item"]
        gift_card.description = request.data["description"]
        gift_card.price = request.data["price"]
        gift_card.occasion = request.data["occasion"]
        gift_card.gift_for = request.data["gift_for"]
        gift_card.name = request.data["name"]
        gift_card.priority = request.data["priority"]

        gift_card.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all gift cards"""
        gift_card = GiftCard.objects.get(pk=pk)
        gift_card.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class GiftCardSerializer(serializers.ModelSerializer):
    """"JSON serializer for gift cards"""
    class Meta:
        model = GiftCard
        fields = ('id', 'board', 'user', 'link', 'image_url', 'item', 'description', 'price', 'occasion', 'gift_for', 'name', 'priority')
