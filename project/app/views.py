from django.http import HttpResponse
from .models import Sonu
from .serializers import SonuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 


def manoj(request):
    return HttpResponse("this is our first app")

class Sonuview(APIView):
    def get(self,request):
        object=Sonu.objects.all()
        serializer=SonuSerializer(object,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class SonuAdd(APIView):
    def post(self,request):
        is_many=isinstance(request.data,list)
        serializer=SonuSerializer(data=request.data,many=is_many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class SonuGetOne(APIView):
    def get(self,request,id):
        try:
            object=Sonu.objects.get(id=id)
        except Sonu.DoesNotExists:
            return Response({"error":"object not found"})
        serializer=SonuSerializer(object)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SonuUpdate(APIView):
    def put(self,request,id):
        try:
            object=Sonu.objects.get(id=id)
        except Sonu.DoesNotExist:
            return Response({"error":"object not found"})
        serializer=SonuSerializer(object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class SonuPatch(APIView):
    def patch(self,request,id):
        try:
            object=Sonu.objects.get(id=id)
        except Sonu.DoesNotExist:
            return Response({"error":"object not found"})
        serializer=SonuSerializer(object,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class SonuDelete(APIView):
    def delete(self,request,id):
        try:
            object=Sonu.objects.get(id=id)
        except Sonu.DoesNotExist:
            return Response({"error":"object not found"},status=status.HTTP_404_NOT_FOUND)
        object.delete()
        return Response({"success":"object deleted successfully"},status=status.HTTP_200_OK)



