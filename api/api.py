import json

from rest_framework.decorators import api_view
from django.http import HttpResponse

# from Model.Student import  std
# from dao.test import getUsers
#
#
# @api_view()
# def listghaza(request):
#
#     return HttpResponse("hello world",content_type="application/json")
# @api_view()
# def student(request):
#     obj=std('ali','gholami',123456798,92255544477)
#     return HttpResponse(json.dumps(obj.__dict__),content_type="application/json")
from dao.test import insertFooddb
@api_view(["POST"])
def registerFood(request):
    Name=json.loads(request.body)["Name"]
    Price=json.loads(request.body)["Price"]
    Type=json.loads(request.body)["Type"]
    Description=json.loads(request.body)["Description"]

    val=insertFooddb(Name, Type, Price, Description)
    return HttpResponse(val,content_type="application/json")

