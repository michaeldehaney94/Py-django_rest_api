from django.http import JsonResponse
from rest_framework.response import Response
from .models import Beverage
from .serializers import BeverageSerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
# get beverage list and add beverage
def beverage_list(request, format=None):
    if request.method == 'GET':
        beverages = Beverage.objects.all()
        serializer = BeverageSerializer(beverages, many=True)
        return JsonResponse({"beverages": serializer.data})

    if request.method == 'POST':
        serializer = BeverageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def beverage_detail(request, id, format=None):

    try:
        beverages = Beverage.objects.get(pk=id)
    except Beverage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request == 'GET':
        serializer = BeverageSerializer(beverages)
        return Response(serializer.data)

    elif request == 'PUT':
        serializer = BeverageSerializer(beverages, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        beverages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
