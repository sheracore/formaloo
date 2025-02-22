from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import AppSerializer

class AppView(APIView):
    permission_classes = [IsAuthenticated]


    @swagger_auto_schema(
        request_body=AppSerializer,
        responses={
            201: openapi.Response(
                "App Created Successfully",
                AppSerializer
            ),
            400: openapi.Response(
                "Validation Error",
                openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "title": openapi.Schema(type=openapi.TYPE_STRING, example="This field is required."),
                        "description": openapi.Schema(type=openapi.TYPE_STRING, example="This field is required."),
                    },
                )
            ),
            401: openapi.Response("Authentication credentials were not provided."),
        },
        operation_description="Create a new app with title, description, price, and category."
    )
    def post(self, request):
        serializer = AppSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={200: openapi.Response("Not implemented")},
        operation_description="Retrieve an app by ID."
    )
    def get(self, request, pk=None):
        return Response({"response": "Not implemented"})

    @swagger_auto_schema(
        request_body=AppSerializer,
        responses={200: openapi.Response("Not implemented")},
        operation_description="Update an app."
    )
    def put(self, request, pk):
        return Response({"response": "Not implemented"})

    @swagger_auto_schema(
        responses={204: openapi.Response("Not implemented")},
        operation_description="Delete an app."
    )
    def delete(self, request, pk):
        return Response({"response": "Not implemented"})
