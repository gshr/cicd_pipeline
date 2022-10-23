from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import asyncio
import requests
import random
import json
from time import perf_counter
from django.http import HttpResponse
# Create your views here.



class GetInfoView(APIView):

    def get(self,request,id):
        url =f'https://reqres.in/api/users/{id}'
        result = requests.get(url)
        return Response(json.loads(result.text))