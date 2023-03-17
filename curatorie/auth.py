from curatorieapi.models import User
from rest_framework import authentication
from rest_framework import exceptions
import firebase_admin.auth as auth


class FirebaseAuthentication(authentication.TokenAuthentication):
    def authenticate(self, request):
        header = request.headers.get('Authorization', None)
        
        if not header:
            return None

        if not header.startswith('Bearer '):
            return None
        
        bearer, _, token = header.partition(' ')
        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token["uid"]
        except Exception as exc:
            raise exceptions.AuthenticationFailed('Bad Id Token', exc)

        try:
            user = User.objects.get(uid=uid)
            return (user, None)

        except User.DoesNotExist as exc:
            raise exceptions.AuthenticationFailed('No such user', exc)
