from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserInfoSerializer
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


class UserInfoView(APIView):
    def get(self, request, *args, **kwargs):
        session_key = request.GET['session_key']
        session = Session.objects.get(session_key=session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        qs = User.objects.get(id=uid)
        serializer = UserInfoSerializer(qs)
        return Response(serializer.data)
