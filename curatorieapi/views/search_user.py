from rest_framework.viewsets import ViewSet
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import User

class SearchUserView(ViewSet):
    def list(self, request):
        """"Handle GET requests for all search users"""
        input = request.GET.get('query', None)
        user_id = request.GET.get('user_id', None)

        if input == '':
            return Response({'message': 'no search provided'}, status=status.HTTP_404_NOT_FOUND)
        users = User.objects.filter(
            Q(first_name__icontains=input) |
            Q(last_name__icontains=input) |
            Q(username__icontains=input) |
            Q(email__icontains=input),
            ~Q(id=user_id)
        )

        serializer = SearchUserSerializer(users, many=True)
        return Response(serializer.data)
    
class SearchUserSerializer(serializers.ModelSerializer):
    """"JSON serializer for search users"""
    class Meta:
        model = User
        fields = ('id', 'uid', 'first_name', 'last_name', 'username', 'image_url', 'email')
