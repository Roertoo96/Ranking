from dataclasses import Field
import json
from unittest import result
from django.shortcuts import render
from .models import BeerPongRankingTable
from django.core import serializers
from .models import BeerPongRankingTable



# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def BeerPongRank(request):
    return render(request, 'BeerPong.html')

# def listview(request):
#     data = BeerPongRankingTable.objects.all()
#     return render(request, 'testpage.html', {'data': data})    

# def testpage(request):
#     data = serializers.serialize("python",BeerPongRankingTable.objects.all())

#     context = {

#         'data':data,

#     }

#     return render(request, 'testpage.html',context)




def testpage(request):
    data = BeerPongRankingTable.objects.all()

    print(data)

    print("-----------------------------")
    print("-----------------------------")
    #data2 = BeerPongRankingTable.objects.filter(id = 1).update(wins=1)

    #data2 = BeerPongRankingTable.objects.filter(id = 3).update(username='rbanew55')
    # print(data2)


    # # if data2 == 'rba':
    # #     print('ja')
    # # else:
    # #     print('nein')

    # # # print(data)

    # print("-----------------------------")
    # print("-----------------------------")



    # # ####### Count the databaseentrys 
    # # data3 = BeerPongRankingTable.objects.count()  # Anzahl Regestrierter User
    # # print(data3) 

    # print("-----------------------------")
    # print("-----------------------------")

    # data4 = BeerPongRankingTable.objects.filter(username = "sdf")
    # data4json =serializers.serialize('json', data4)
    # print('Data4')
    # print(data4json)


    # print("-----------------------------")
    # print("-----------------------------")

    # data5 = BeerPongRankingTable.objects.get(username = 'rba')

    # print(data5)




    return render(request, 'testpage.html', locals())








def addmatch(request):
    resultaddmatch=BeerPongRankingTable.objects.all()
    #print(result)
    context = {
        'resultaddmatch': resultaddmatch
    }



    if request.method == 'POST':
        pointsteam1 = request.POST['goalsteam1']
        pointsteam2 = request.POST['goalsteam2']
        usernameIDt1n1 = request.POST['nameIDt1n1']
        print(usernameIDt1n1)
        usernameIDt1n2 = request.POST['nameIDt1n2']
        print(usernameIDt1n2)
        usernameIDt2n1 = request.POST['nameIDt2n1']
        usernameIDt2n2 = request.POST['nameIDt2n2']
       #print(pointsteam1, pointsteam2, usernameIDt1n1, usernameIDt1n2, usernameIDt2n1, usernameIDt2n2)


        DatanameIDt1n1 = BeerPongRankingTable.objects.filter(username = usernameIDt1n1)
        # print(DatanameIDt1n1)
        DatanameIDt1n1json = serializers.serialize('json', DatanameIDt1n1)
        DatanameIDt1n1list = json.loads(DatanameIDt1n1json)
        # print(DatanameIDt1n1list)
        t1n1gusername = DatanameIDt1n1list[0]['fields']['username']
        t1n1games = DatanameIDt1n1list[0]['fields']['games']
        # print(t1n1games, t1n1gusername)
        t1n1gamesnew = t1n1games + 1
        # print(t1n1gamesnew)
        Dataend = BeerPongRankingTable.objects.filter(username = t1n1gusername).update(games = t1n1gamesnew)




        DatanameIDt1n2 = BeerPongRankingTable.objects.filter(username = usernameIDt1n2)
        print(DatanameIDt1n2)
        DatanameIDt1n2json = serializers.serialize('json', DatanameIDt1n2)
        DatanameIDt1n2list = json.loads(DatanameIDt1n2json)
        print(DatanameIDt1n2list)
        t1n2gusername = DatanameIDt1n2list[0]['fields']['username']
        t1n2games = DatanameIDt1n2list[0]['fields']['games']
        print(t1n2games, t1n2gusername)
        t1n2gamesnew = t1n2games + 1
        print(t1n2gamesnew)
        Dataend2 = BeerPongRankingTable.objects.filter(username = t1n2gusername).update(games = t1n2gamesnew)
        print(Dataend2)


    else:
        print('keine Daten')





    return render(request, 'addmatch.html', context)





def adduser(request):
    if request.method == 'POST':
        BeerPongRankingTable.objects.create(username = request.POST['username'])
        print('Received data:', request.POST['username'])
    return render(request, 'adduser.html')