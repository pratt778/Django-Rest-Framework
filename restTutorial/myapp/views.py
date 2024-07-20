from django.shortcuts import render
from .models import CarList
from django.http import JsonResponse
from .api_file.serializers import SerializeData
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework import status
# import json
# Create your views here.
# def carlist(request):
#     mycar = CarList.objects.all()
#     data={
#         'car':list(mycar.values())
#     }
#     mydata = json.dumps(data)
    #you can also use http response but it takes few extra lines of code.
    # return HttpResponse(mydata,content_type='application/json')
    # return JsonResponse(data)

# def cardetails(request,pk):
#     mycar = CarList.objects.get(id=pk)
#     data={
#         'name':mycar.name,
#         'description':mycar.desc,
#         'active':mycar.active
#     }
#     return JsonResponse(data)


@api_view(['GET','POST'])
def carlist(request):
    if request.method=="GET":
        mycar = CarList.objects.all()
        serializedata=SerializeData(mycar,many=True)
        return Response(serializedata.data)
    if request.method=="POST":
        serialize=SerializeData(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)



@api_view(['GET','PUT','DELETE'])
def cardetails(request,pk):
    if request.method=='GET':
        try:
            mycar = CarList.objects.get(id=pk)
        except:
            return Response({"Error":"Car not found"},status=status.HTTP_404_NOT_FOUND)
        serializer=SerializeData(mycar)
        return Response(serializer.data)
    if request.method=='PUT':
        mycar = CarList.objects.get(id=pk)
        serialize=SerializeData(mycar,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        mycar = CarList.objects.get(id=pk)
        mycar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)