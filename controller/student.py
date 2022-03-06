import json as j

from dao.studentDao import studentActions
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['POST'])
def regStudent(req):
    FirstName = j.loads(req.body)['FirstName']   # ,[FirstName]
    LastName = j.loads(req.body)['LastName']      #       ,[LastName]
    BirthdayDate = j.loads(req.body)['BirthdayDate']   #       ,[BirthdayDate]
    Gender = j.loads(req.body)['Gender']     #       ,[Gender]
    NationalCode = j.loads(req.body)['NationalCode']   #       ,[NationalCode]
    BirthdayPlace = j.loads(req.body)['BirthdayPlace']    #    ,[BirthdayPlace]
    Weight = j.loads(req.body)['Weight']            #       ,[Weight]
    Height = j.loads(req.body)['Height']        #       ,[Height]
    PreEducation = j.loads(req.body)['PreEducation']  #       ,[PreEducation]
    DominantHand = j.loads(req.body)['DominantHand']         #       ,[DominantHand]
    Insurance = j.loads(req.body)['Insurance']      #       ,[FamilyMembers]
    FamilyMembers = j.loads(req.body)['FamilyMembers']
    MemberNum= j.loads(req.body)['MemberNum']      #       ,[MemberNum]
    Supervisor = j.loads(req.body)['Supervisor']     #       ,[Supervisor]
    SpecialDisease = j.loads(req.body)['SpecialDisease']   #       ,[SpecialDisease]
    Medicine = j.loads(req.body)['Medicine']   #       ,[Medicine]
    HomeAddress = j.loads(req.body)['HomeAddress']    #       ,[HomeAddress]
    Country = j.loads(req.body)['Country']   #       ,[Country]
    City = j.loads(req.body)['City']                                           #       ,[City]
    result = studentActions.insertStudent(FirstName, LastName, BirthdayDate, Gender, NationalCode, BirthdayPlace, Weight,Height, PreEducation, DominantHand, Insurance, FamilyMembers, MemberNum, Supervisor, SpecialDisease, Medicine, HomeAddress, Country, City)


    return HttpResponse(result, content_type='application/json')