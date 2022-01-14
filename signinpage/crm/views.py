import json
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

# Create your views here.
def sign_in(request):
    return render(request,'sign_in.html')

@api_view(['POST'])
def register_user(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    re_pasword = request.data.get("re_password")

    if password == re_pasword:
        data = User.objects.create(username=username,email=email,password=make_password(re_pasword))
        return JsonResponse({'success':True,'Message':"Successfully created Account...!"})
    else:
        return JsonResponse({'success':False,'Message':"Password Doesn't matched"})
    