from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from curatorieapi.models import Type

class TypeView(ViewSet):

   def list(self, request):
        """"Handle GET requests for all types"""
        types = Type.objects.all()

        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)

class TypeSerializer(serializers.ModelSerializer):
    """"JSON serializer for types"""
    class Meta:
        model = Type
        fields = ('id', 'name')
