from django.shortcuts import render
from .models import CustomUser
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView




class TokenObtainPairViewExtend(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Adding custom climes 
        token['id'] = user.id
        token['name'] = user.name
        token['admin'] = user.is_superuser

        if token:
            return token
        else:
            return Response("False")
        

class MytokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairViewExtend


@api_view(['POST', 'GET'])
def Students(request):
    if request.method == "POST":
        uname = request.data.get('username')
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = CustomUser.objects.get(username = uname)
                if user:
                    return Response({'message':"Username already taken "})
            except:
                serializer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'message':'wrong credentials'})
    else:
        users = CustomUser.objects.all()
        serializer = StudentSerializer(users, many = True)
        return Response(serializer.data)
    

@api_view(['PUT', 'DELETE', 'GET'])
def Crud(request, id):
    try:
        user = CustomUser.objects.get(id=id)
    except:
        return Response({'message':'Item not found'})
    
    if request.method == "GET":
        serializer=StudentSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = StudentSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'message':'invalid input'})
    else:
        user.delete()
        return Response(status=status.HTTP_200_OK)
