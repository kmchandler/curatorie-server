from rest_framework.decorators import api_view
from rest_framework.response import Response
from curatorieapi.models import User


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has associated User

    Method arguments:
      request -- The full HTTP request object
    '''

    uid = request.data['uid']

    try:
        user = User.objects.get(uid=uid)

        data = {
            'id': user.id,
            'uid': user.uid,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            "image_url": user.image_url,
            'email': user.email,
            'color_scheme': user.color_scheme
        }
        return Response(data)
    except:
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    user = User.objects.create(
        uid=request.data['uid'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        username=request.data['username'],
        image_url=request.data['image_url'],
        email=request.data['email'],
        color_scheme=request.data['color_scheme']
    )

    data = {
            'id': user.id,
            'uid': user.uid,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            "image_url": user.image_url,
            'email': user.email,
            'color_scheme': user.color_scheme
    }
    return Response(data)
