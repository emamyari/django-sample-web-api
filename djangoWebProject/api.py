import json
import pyodbc
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET'])
def stdList(request):
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=46.34.161.23,13433;DATABASE=dbTest;UID=sa;PWD=111@a')
    cursor = connection.cursor()

    cursor.execute("SELECT *  FROM Students")

    rows=cursor.fetchall()

    connection.close()
    list=[]
    for r in rows:
        obj=student(r[0],r[1],r[2])
        list.append(obj.__dict__)


    return HttpResponse(json.dumps(list),content_type='application/json')







class student():
    def __init__(self,name,family,bd):
        self.name=name
        self.family=family
        self.bd=bd
