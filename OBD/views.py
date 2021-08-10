from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django import template
 
from OBD.models import Obd
from OBD.serializers import ObdSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Obd.objects.all()
        
        OrgID = request.GET.get('OrgID', None)
        if OrgID is not None:
            tutorials = tutorials.filter(title__icontains=OrgID)
        
        tutorials_serializer = ObdSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ObdSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Obd.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Obd.objects.get(pk=pk)
    except Obd.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = ObdSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = ObdSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Obd.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = ObdSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    

def TableView(request):
    return render(request,"table.html")