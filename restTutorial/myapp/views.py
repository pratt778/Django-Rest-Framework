from django.shortcuts import render
from .models import CarList,ShowroomList,Rating
from django.http import JsonResponse
from .api_file.serializers import SerializeData,ShowroomSerializer,RatingSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes,APIView
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
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
    
class ShowroomView(APIView):
    # authentication_classes=[BasicAuthentication]
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    permission_classes=[IsAdminUser]

    def get(self,request):
        showroom = ShowroomList.objects.all()
        myroom = ShowroomSerializer(showroom,many=True,context={'request': request})
        return Response(myroom.data)
    def post(self,request):
        showroom = ShowroomSerializer(data=request.data)
        if showroom.is_valid():
            showroom.save()
            return Response(showroom.data)
        else:
            return Response(showroom.errors)
        
class Showroomdetail(APIView):
    def get(self,request,pk):
        showroom = ShowroomList.objects.get(id=pk)
        serializer = ShowroomSerializer(showroom)
        return Response(serializer.data)
    def put(self,request,pk):
        showroom = ShowroomList.objects.get(id=pk)
        serialize = ShowroomSerializer(showroom,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize._errors)
    def delete(self,request,pk):
        showroom = ShowroomList.objects.get(id=pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewView(APIView):
    
    def get(self,request):
        allrating = Rating.objects.all()
        serializer=RatingSerializer(allrating,many=True)
        return Response(serializer.data)

    