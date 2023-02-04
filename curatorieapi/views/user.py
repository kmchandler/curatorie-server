from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import User

class UserView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single user
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
 
    def list(self, request):
        """"Handle GET requests for all users"""
        users = User.objects.all()

        user_id = request.query_params.get('uid', None)
        if user_id is not None:
            users = users.filter(uid=user_id)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized user instance
        """

        user = User.objects.create(
            uid=request.data["uid"],
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            username=request.data["username"],
            image_url=request.data["image_url"],
            email=request.data["email"],
            color_scheme=request.data["color_scheme"],
        )
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a user

        Returns:
            Response -- Empty body with 204 status code
        """

        user = User.objects.get(pk=pk)
        user.uid = request.data["uid"]
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.username = request.data["username"]
        user.image_url = request.data["image_url"]
        user.email = request.data["email"]
        user.color_scheme = request.data["color_scheme"]

        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all users"""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class UserSerializer(serializers.ModelSerializer):
    """"JSON serializer for users"""
    class Meta:
        model = User
        fields = ('id', 'uid', 'first_name', 'last_name', 'username', 'image_url', 'email', 'color_scheme')
