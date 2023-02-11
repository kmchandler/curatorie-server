from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import Icon

class IconView(ViewSet):

   def list(self, request):
        """"Handle GET requests for all icons"""
        icons = Icon.objects.all()

        serializer = IconSerializer(icons, many=True)
        return Response(serializer.data)

class IconSerializer(serializers.ModelSerializer):
    """"JSON serializer for icons"""
    class Meta:
        model = Icon
        fields = ('id', 'name')
