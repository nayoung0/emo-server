from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class OnePersonAPIView(APIView):
    def get(self, request, format=None):
        data = {
            "id": 1,
            "name": "John Doe",
            "age": 25,
            "city": "Sample City"
        }
        return Response(data)
