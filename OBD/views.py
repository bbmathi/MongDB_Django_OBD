from typing import List

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django import template
 
from OBD.models import Obd
from OBD.serializers import ObdSerializer
from rest_framework.decorators import api_view

from .databaseconfig import Databaseconfig
from .import databaseconfig as dbc
import json


@api_view(['GET', 'POST', 'DELETE'])
def obd_list(request):
    if request.method == 'GET':
        connection = Databaseconfig()
        connection.connect()
        db = dbc.client["OBD"]
        documents = db['OBD_Device_Status'].find()
        print("document readed" , documents)
        listOfDocuments: List = []
        for document in documents:
            listOfDocuments.append(document)

        strindata = json.dumps(listOfDocuments,default=str)
        jsondata = json.loads(strindata)

        return JsonResponse(jsondata,safe=False)

        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        obd_data = JSONParser().parse(request)
        obd_serializer = ObdSerializer(data=obd_data)
        if obd_serializer.is_valid():
            obd_serializer.save()
            return JsonResponse(obd_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(obd_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Obd.objects.all().delete()
        return JsonResponse({'message': '{} OBD Data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


def obd_list_history(request):
    if request.method == 'GET':
        connection = Databaseconfig()
        connection.connect()
        db = dbc.client["OBD"]
        documents = db['OBD_Device_Status_History'].find()
        print("documents read", documents)
        listOfDocuments: List = []
        for document in documents:
            listOfDocuments.append(document)

        strindata = json.dumps(listOfDocuments, default=str)
        jsondata = json.loads(strindata)

        return JsonResponse(jsondata, safe=False)

        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        obd_data = JSONParser().parse(request)
        obd_serializer = ObdSerializer(data=obd_data)
        if obd_serializer.is_valid():
            obd_serializer.save()
            return JsonResponse(obd_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(obd_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Obd.objects.all().delete()
        return JsonResponse({'message': '{} OBD Data were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def obd_detail(request, pk):
    try: 
        obd_data = Obd.objects.get(pk=pk)
    except Obd.DoesNotExist:
        return JsonResponse({'message': 'The OBD Data does not exist'}, status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET': 
        obd_serializer = ObdSerializer(obd_data)
        return JsonResponse(obd_serializer.data)
 
    elif request.method == 'PUT': 
        obd_data = JSONParser().parse(request)
        obd_serializer = ObdSerializer(obd_data, data=obd_data)
        if obd_serializer.is_valid():
            obd_serializer.save()
            return JsonResponse(obd_serializer.data)
        return JsonResponse(obd_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE': 
        obd_data.delete()
        return JsonResponse({'message': 'OBD Data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def obd_list_published(request):
    data = Obd.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = ObdSerializer(data, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    

def TableView(request):
    return render(request,"table.html")
def MapView(request):
    return render(request,"map.html")
def ChartView(request):
    return render(request,"dashboard.html")
def CarDetails(request):
    return render(request,"car_page.html")
def AlertView(request):
    return render(request,"alert_view.html")