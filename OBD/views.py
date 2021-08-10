from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django import template
 
from OBD.models import Obd
from OBD.serializers import ObdSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def obd_list(request):
    if request.method == 'GET':
        data = Obd.objects.all()
        
        OrgID = request.GET.get('OrgID', None)
        if OrgID is not None:
            data = data.filter(title__icontains=OrgID)
        
        obd_serializer = ObdSerializer(data, many=True)
        return JsonResponse(obd_serializer.data, safe=False)
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
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def obd_detail(request, pk):
    try: 
        tutorial = Obd.objects.get(pk=pk)
    except Obd.DoesNotExist:
        return JsonResponse({'message': 'The OBD Data does not exist'}, status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET': 
        obd_serializer = ObdSerializer(tutorial)
        return JsonResponse(obd_serializer.data)
 
    elif request.method == 'PUT': 
        obd_data = JSONParser().parse(request)
        obd_serializer = ObdSerializer(tutorial, data=obd_data)
        if obd_serializer.is_valid():
            obd_serializer.save()
            return JsonResponse(obd_serializer.data)
        return JsonResponse(obd_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
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