from django.shortcuts import render
from msrest import Serializer
from rest_framework.views import APIView, Response
from .serializers import SignUpSerializer
from .models import SignUp
# Create your views here.
class CreateSignUP(APIView):
    def post(self, request, format=None):
        serializer= SignUpSerializer(data=request.data)
        print(serializer)
        email = request.data["email"]
        if_email = SignUp.objects.filter(email=email).exists() 
        # print(if_email)
        if if_email:
            return Response({"message": f"The user with {email} already exists."})
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response (serializer.errors)
class GetAllData(APIView):
    def get(self, request, format=None):
        try:
            signup = SignUp.objects.all()
            serializer=SignUpSerializer(signup, many=True)
            return Response(serializer.data)
        except SignUp.DoesNotExist:
            return Response(serializer.errors)

class DeleteData(APIView):
    def delete(self, request,pk,format=None):
        # print("------------------")
        try:
            signup=SignUp.objects.get(pk=pk)
            signup.delete()
            return Response({"message":f"The data with the id {pk} is deleted."})
        except SignUp.DoesNotExist:
            return Response({"message":"The model does not exist."})

class DoLogin(APIView):
    def post(self, request, format=None):
        email = request.data["email"]
        password=request.data["password"]
        user= SignUp.objects.filter(email = email).exists()
        # print(user)
        if user:
            user_password = SignUp.objects.filter(password = password).exists()
            print(user_password)
            if user_password:
                return Response({"message": "ok"})
            else:
                return Response({"message": "Password does not match"})
        else:
            return Response ({"message": "The user does not exist. Please sign up first"})

        
 

    
