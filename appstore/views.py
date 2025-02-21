from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .serializers import AppSerializer

class AppView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AppSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        Response({"response": "Not implemented"})

    def put(self, request, pk):
        Response({"response": "Not implemented"})

    def delete(self, request, pk):
        Response({"response": "Not implemented"})
