import json
from django.http import HttpResponse
from rest_framework.decorators import api_view

def stList(request):
    st=Student("ali","rezaei",1384,9123420142,'zanjan')
    dst=st.__dict__
    return HttpResponse(json.dumps(dst),content_type='application/json')

@api_view(['POST'])
def tList(request):
    year=request.data['year']
    name=request.data['name']
    st1=Teacher("abolfazl","javadi",1360,91111111111,'rasht')
    st2=Teacher("reza","bayat",1372,91111111111,'zanjan')
    st3=Teacher("saeed","mohammadi",1370,91111111111,'tehran')
    st4=Teacher("ali","aliyari",1370,91111111111,'tehran')
    st5=Teacher("mohammad","javadi",1371,91111111111,'mashhad')
    list=[]
    if st1.bd>=year and st1.name==name:
        list.append(st1.__dict__)
    if st2.bd>=year  and st2.name==name:
        list.append(st2.__dict__)
    if st3.bd>=year  and st3.name==name:
        list.append(st3.__dict__)
    if st4.bd>=year  and st4.name==name:
        list.append(st4.__dict__)
    if st5.bd>=year  and st5.name==name:
        list.append(st5.__dict__)
    return HttpResponse(json.dumps(list),content_type='application/json')

@api_view(['GET'])
def techList(request):
    year= int(request.query_params['year'])
    name=request.query_params['name']
    st1=Teacher("abolfazl","javadi",1360,91111111111,'rasht')
    st2=Teacher("reza","bayat",1372,91111111111,'zanjan')
    st3=Teacher("saeed","mohammadi",1370,91111111111,'tehran')
    st4=Teacher("ali","aliyari",1370,91111111111,'tehran')
    st5=Teacher("mohammad","javadi",1371,91111111111,'mashhad')
    list=[]
    if st1.bd>=year and st1.name==name:
        list.append(st1.__dict__)
    if st2.bd>=year  and st2.name==name:
        list.append(st2.__dict__)
    if st3.bd>=year  and st3.name==name:
        list.append(st3.__dict__)
    if st4.bd>=year  and st4.name==name:
        list.append(st4.__dict__)
    if st5.bd>=year  and st5.name==name:
        list.append(st5.__dict__)
    return HttpResponse(json.dumps(list),content_type='application/json')






class Student():
    def __init__(self,name,family,bd,tel,city):
        self.name=name
        self.family=family
        self.bd=bd
        self.tel=tel
        self.city=city

class Teacher():
    def __init__(self,name,family,bd,tel,city):
        self.name=name
        self.family=family
        self.bd=bd
        self.tel=tel
        self.city=city
