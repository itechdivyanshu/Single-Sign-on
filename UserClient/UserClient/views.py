# from django.shortcuts import render
from django.http import HttpResponse
import requests
# from django.contrib.sessions.models import Session


# Create your views here.
def home(request):
    session_key = request.COOKIES.get('sessionid')
    if session_key is not None:
        response = requests.get(
            'http://localhost:8000/',
            params={'session_key': session_key},
        )
        r = response.json()
        username = r['username']
        return HttpResponse(f"Hello {username}")
    else:
        return HttpResponse("Hello You Havent Signed in")
    # return render(request, 'website/home.html', dict1)
