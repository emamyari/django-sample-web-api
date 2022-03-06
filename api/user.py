# import json
# from django.http import HttpResponse
# import pandas as pd
# from rest_framework.decorators import api_view
#
# from Model.Users import User
# from dao.test import sqlApi
# from api.student import student
#
#
# @api_view(['GET'])
# def test(request):
#
#     # obj1=User('ali','vvv')
#     # obj2=User('amir','karimi')
#     # obj3=User('mohamad','bageri')
#     # obj4=User('bager','soleimani')
#     # list=[obj1,obj2,obj3,obj4]
#
#     return HttpResponse(json.dumps(list,default=lambda o:o.__dict__,sort_keys=False),content_type='application/json')