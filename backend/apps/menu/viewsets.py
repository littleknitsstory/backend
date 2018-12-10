from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializer import MenuSerializer
from .models import MenuItems
from rest_framework.response import Response
from django.http import Http404


class MenuAPIViewSet(ModelViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MenuSerializer


class MenuAPICRUD(APIView):

    queryset = MenuItems.objects.all()


    def get_object(self, pk):
        try:
            return MenuItems.objects.get(pk=pk)
        except MenuItems.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MenuSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MenuSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)