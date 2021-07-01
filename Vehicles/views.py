from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
import rest_framework
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache,caches


def redirectpage(request):    ####listpage'e redirect ediyor
    return redirect('listPage')

@api_view(['GET','POST']) ####################Listpagede databasedeki bütün araçları gösteriyor###########################
def listPage(request):
    
    if request.method == 'GET' :
        List = []               #######cacheden araç bilgilerini liste olarak almak için oluşturulmuş boş liste ###
        if cache.get('counter'): ######cache'den' araçları liste olarak almak için for döngüsünde iterate etmek amacıyla cache'e 'counter' anahtar değerli bir atama yapılıyor. 
            pass                  #########'counter'ın tuttuğu değer databasedeki en yüksek id numaralı aracın id'si. 
        else:
            counter = vehicle.objects.last()    
            cache.set('counter',counter.id)
            
        counter = cache.get('counter')
        for i in range(1,counter+1):
            List.append(i) ##################Boş listeye en yüksek id ye kadar bütün id ler ekleniyor
            if cache.get(i) :
                print('data from cache')
            else:
                try:   #######burdada eğer cache'de bu id numaralı araç yoksa araç bu id'ye göre set ediliyor. Ancak eğer bu id numaralı araç toptan silindiyse(DoesNotExist) print ile terminale 'bu id no yok' yazılıyor
                    vehicle_with_idnumber_i = vehicle.objects.get(id=i)
                    cache.set(i,vehicle_with_idnumber_i)
                    print('data from db')
                except vehicle.DoesNotExist:
                    print('bu id no ile yok')

                
        vehicles = cache.get_many(List)
        print(vehicles)    
        serializer = vehicleSerializer(vehicles.values() , many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        
        serializer = vehicleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            vehiclePOSTED = vehicle.objects.last()
            cache.set(vehiclePOSTED.id,vehiclePOSTED)   
            cache.set('counter',vehiclePOSTED.id) #### burdada post edilen data en yüksek id değerine sahip olacağı için counter post edilen datanın id'sine ayarlanıyor
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def vehicle_model_detail(request,pk):
    vehicleDetail = cache.get(pk) 

    if request.method == 'GET' :        
        serializer = vehicleSerializer(vehicleDetail)
        return Response(serializer.data)
    
    
    elif request.method =='PUT':
         
        serializer = vehicleSerializer(vehicleDetail, data=request.data)
        print(serializer)
        if serializer.is_valid():
            cache.delete(pk)
            serializer.save()
            vehicleChanged = vehicle.objects.get(pk=pk)
            cache.set(pk,vehicleChanged)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':
        cache.delete(pk)
        vehicleDetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







# @csrf_exempt
# def vehicle_model_detail(request,pk):
#     try:
#         vehicle_modelDetail = vehicle_model.objects.get(pk=pk)
#     except vehicle_model.DoesNotExist:
#         return HttpResponse(status=400)
    
#     if request.method == 'GET' :
#         serializer = vehicle_model_Serializer(vehicle_modelDetail)
#         return JsonResponse(serializer.data)
    
#     elif request.method =='PUT':  
#         data = JSONParser().parse(request)
#         serializer = vehicle_model_Serializer(vehicle_modelDetail, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         vehicle_modelDetail.delete()
#         return HttpResponse(status=204)




# @csrf_exempt
# def listPage(request):
    
#     if request.method == 'GET' :
#         vehicle_models = vehicle_model.objects.all()
#         serializer = vehicle_model_Serializer(vehicle_models , many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method =='POST':
#         data = JSONParser().parse(request)
#         serializer = vehicle_model_Serializer(data=data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
 
#         return JsonResponse(serializer.errors, status=400)