from django.middleware import csrf
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_csrf_token(request):
    token = {
        'csrf_token': csrf.get_token(request)
    }

    return Response(token)
