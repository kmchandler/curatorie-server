from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import PurchaseCard

class PurchaseCardView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single purchase card
        """
        try:    
            purchase_card = PurchaseCard.objects.get(pk=pk)
            serializer = PurchaseCardSerializer(purchase_card)
            return Response(serializer.data)
        except PurchaseCard.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
 
    def list(self, request):
        """"Handle GET requests for all purchase cards"""
        purchase_cards = PurchaseCard.objects.all()

        serializer = PurchaseCardSerializer(purchase_cards, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized purchase card instance
        """
        purchase_card = PurchaseCard.objects.create(
            id=request.data["id"],
            board=request.data["board"],
            user=request.data["user"],
            link=request.data["link"],
            image_url=request.data["image_url"],
            item=request.data["item"],
            description=request.data["description"],
            price=request.data["price"],
            priority=request.data["priority"]
        )
        serializer = PurchaseCardSerializer(purchase_card)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a purchase card

        Returns:
            Response -- Empty body with 204 status code
        """

        purchase_card = PurchaseCard.objects.get(pk=pk)
        purchase_card.board = request.data["board"],
        purchase_card.user = request.data["user"],
        purchase_card.link = request.data["link"],
        purchase_card.image_url = request.data["image_url"],
        purchase_card.item = request.data["item"],
        purchase_card.description = request.data["description"],
        purchase_card.price = request.data["price"],
        purchase_card.priority = request.data["priority"]

        purchase_card.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all purchase cards"""
        purchase_card = PurchaseCard.objects.get(pk=pk)
        purchase_card.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class PurchaseCardSerializer(serializers.ModelSerializer):
    """"JSON serializer for purchase cards"""
    class Meta:
        model = PurchaseCard
        fields = ('id', 'board', 'user', 'link', 'image_url', 'item', 'description', 'price', 'priority')
