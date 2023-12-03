from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class OnePersonAPIView(APIView):
    def get(self, request, format=None):
        data = {
            "id": 1,
            "name": "integerji",
            "age": 28,
            "city": "Gwanak-gu"
        }
        return Response(data)
    
    def post(self, request, format=None):
        data = {
            "id": 2,
            "name": "nayoung0",
            "age": 29,
            "city": "Gwanak-gu"
        }
        return Response(data)
