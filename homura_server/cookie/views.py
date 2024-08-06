from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse


@api_view(['POST'])
def createCookie(request, cookie_name):
    cookie = request.POST.get(cookie_name)
    response = HttpResponse()

    if cookie_name not in request.COOKIES or cookie != request.COOKIES.get(cookie):
        response.set_cookie(cookie_name, cookie,
                            max_age=1*24*60*60)

    return response


@api_view(['GET'])
def getCookie(request, cookie_name):
    cookie = ''
    if cookie_name in request.COOKIES:
        cookie = request.COOKIES.get(cookie_name)
    else:
        cookie = 'null'

    return Response({cookie_name: cookie})


@api_view(['DELETE'])
def deleteCookie(request, cookie_name):
    response = HttpResponse()
    if cookie_name in request.COOKIES:
        try:
            response.delete_cookie(cookie_name)
            return response
        except Exception as ex:
            print(ex)
    else:
        return response
