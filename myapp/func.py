import json

from django.shortcuts import render
import pyodbc
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
def page(request):
    connection= pyodbc.connect('DRIVER={ODBC DRIVER 17 FOR SQL SERVER};Server=192.168.1.199;Database=emamyari;Port=1433;UID=sa;PWD=123456@a')
    cursor=connection.cursor()
    name=request.data['name']
    cursor.execute("select * from person where Name=?",name)
    data=cursor.fetchall()
    lst=[]
    for item in data:
        myDictionary={'firstName':item[0],'lastName':item[1],'tel':item[2],'nationalCode':item[3]}
        lst.append(myDictionary)

    a=render(request,'page1.html',context={'data':lst} )
    return a

def page2(request):
    a=render(request,'page2.html')
    return a