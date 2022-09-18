from dataclasses import Field
from email import message
import json
from unittest import result
from django.shortcuts import render
from .models import BeerPongRankingTable
from django.core import serializers
from .models import BeerPongRankingTable
import discord
from .discord import DCTOKEN



# def discordbot(pointsteam1, pointsteam2, usernameIDt1n1, usernameIDt1n2, usernameIDt2n1, usernameIDt2n2):
#     intents = discord.Intents.default()
#     intents.message_content = True

#     if pointsteam1 >= pointsteam2:
#         winner = 'Team1'
#     elif pointsteam1 <= pointsteam2:
#         winner = 'Team2'



#     client = discord.Client(intents=intents)


#     @client.event
#     async def on_ready():
#         print('Wir sind eingeloggt als User {}'.format(client.user.name))
#         client.loop.create_task(send())
#         client.loop.create_task(status_task())

#     async def status_task():
#          while True:
#              await client.change_presence(activity=discord.Game('BeerPongBot'), status=discord.Status.online)


#     async def send():
#         await client.get_channel(1019713905766969354).send("Folgendes Spiel wurde hinzugefügt: Team 1: " + usernameIDt1n1 + " und " + usernameIDt1n2 +" mit " +pointsteam1 + " Punkten. " + 
#         " Team 2: " + usernameIDt2n1 + " und " + usernameIDt2n2 + " mit " + pointsteam2 + " Punkten." +
#          " Der Gewinner ist: " + winner )


#     client.run(DCTOKEN)


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
    aaa = BeerPongRankingTable.objects.order_by('-wins')
    for i in range(1, len(aaa) + 1):
        aaa[i - 1].rank = i
        aaa[i - 1].save()
        print('aaa[i].wins', aaa[i-1].wins, type(aaa))
        
    #context2 = {'fff': aaa}


    print("-----------------------------")
    print("-----------------------------")
    #data2 = BeerPongRankingTable.objects.filter(id = 1).update(wins=1)

    # data2 = BeerPongRankingTable.objects.filter(id = 1).update(username='RBA')
    # data2 = BeerPongRankingTable.objects.filter(id = 2).update(username='CHW')
    # data2 = BeerPongRankingTable.objects.filter(id = 3).update(username='CJ')
    # data2 = BeerPongRankingTable.objects.filter(id = 4).update(username='NBA')
    # data2 = BeerPongRankingTable.objects.filter(id = 5).update(username='FN')
    # data2 = BeerPongRankingTable.objects.filter(id = 6).update(username='JS')
    # data2 = BeerPongRankingTable.objects.filter(id = 7).update(username='PHA')
    #BeerPongRankingTable.objects.filter(id=11).delete()



    # # ####### Count the databaseentrys 
    # # data3 = BeerPongRankingTable.objects.count()  # Anzahl Regestrierter User

    # data4 = BeerPongRankingTable.objects.filter(username = "sdf")
    # data4json =serializers.serialize('json', data4)


    # data5 = BeerPongRankingTable.objects.get(username = 'rba')


    return render(request, 'testpage.html', locals())








def addmatch(request):
    resultaddmatch=BeerPongRankingTable.objects.all()
    #print(result)
    context = {
        'resultaddmatch': resultaddmatch
    }



    rank = BeerPongRankingTable.objects.filter()

    if request.method == 'POST':
        pointsteam1 = request.POST['goalsteam1']
        pointsteam2 = request.POST['goalsteam2']
        usernameIDt1n1 = request.POST['nameIDt1n1']
        usernameIDt1n2 = request.POST['nameIDt1n2']
        usernameIDt2n1 = request.POST['nameIDt2n1']
        usernameIDt2n2 = request.POST['nameIDt2n2']

        DatanameIDt1n1 = BeerPongRankingTable.objects.filter(username = usernameIDt1n1)
        DatanameIDt1n1json = serializers.serialize('json', DatanameIDt1n1)
        DatanameIDt1n1list = json.loads(DatanameIDt1n1json)
        t1n1gusername = DatanameIDt1n1list[0]['fields']['username']
        t1n1games = DatanameIDt1n1list[0]['fields']['games']
        t1n1gamesnew = t1n1games + 1
        BeerPongRankingTable.objects.filter(username = t1n1gusername).update(games = t1n1gamesnew)

        DatanameIDt1n2 = BeerPongRankingTable.objects.filter(username = usernameIDt1n2)
        DatanameIDt1n2json = serializers.serialize('json', DatanameIDt1n2)
        DatanameIDt1n2list = json.loads(DatanameIDt1n2json)
        t1n2gusername = DatanameIDt1n2list[0]['fields']['username']
        t1n2games = DatanameIDt1n2list[0]['fields']['games']
        t1n2gamesnew = t1n2games + 1
        BeerPongRankingTable.objects.filter(username = t1n2gusername).update(games = t1n2gamesnew)

        DatanameIDt2n1 = BeerPongRankingTable.objects.filter(username = usernameIDt2n1)
        DatanameIDt2n1json = serializers.serialize('json', DatanameIDt2n1)
        DatanameIDt2n1list = json.loads(DatanameIDt2n1json)
        t2n1gusername = DatanameIDt2n1list[0]['fields']['username']
        t2n1games = DatanameIDt2n1list[0]['fields']['games']
        t2n1gamesnew = t2n1games + 1
        BeerPongRankingTable.objects.filter(username = t2n1gusername).update(games = t2n1gamesnew)

        DatanameIDt2n2 = BeerPongRankingTable.objects.filter(username = usernameIDt2n2)
        DatanameIDt2n2json = serializers.serialize('json', DatanameIDt2n2)
        DatanameIDt2n2list = json.loads(DatanameIDt2n2json)
        t2n2gusername = DatanameIDt2n2list[0]['fields']['username']
        t2n2games = DatanameIDt2n2list[0]['fields']['games']
        t2n2gamesnew = t2n2games + 1
        BeerPongRankingTable.objects.filter(username = t2n2gusername).update(games = t2n2gamesnew)

        print(pointsteam1, pointsteam2)
        
        if pointsteam1 >= pointsteam2:
            t1n1wins = DatanameIDt1n1list[0]['fields']['wins']
            t1n2wins = DatanameIDt1n2list[0]['fields']['wins']
            t1n1winsnew = t1n1wins +1
            t1n2winsnew = t1n2wins +1
            BeerPongRankingTable.objects.filter(username = t1n1gusername).update(wins = t1n1winsnew)
            BeerPongRankingTable.objects.filter(username = t1n2gusername).update(wins = t1n2winsnew)
        elif pointsteam1 <= pointsteam2:
            t2n1wins = DatanameIDt2n1list[0]['fields']['wins']
            t2n2wins = DatanameIDt2n2list[0]['fields']['wins']
            t2n1winsnew = t2n1wins +1
            t2n2winsnew = t2n2wins +1
            BeerPongRankingTable.objects.filter(username = t2n1gusername).update(wins = t2n1winsnew)
            BeerPongRankingTable.objects.filter(username = t2n2gusername).update(wins = t2n2winsnew)

        #discordbot(pointsteam1,pointsteam2, usernameIDt1n1, usernameIDt1n2, usernameIDt2n1, usernameIDt2n2)

    else:
        print('keine Daten')





    return render(request, 'addmatch.html', context)





def adduser(request):
    if request.method == 'POST':
        BeerPongRankingTable.objects.create(username = request.POST['username'])
        print('Received data:', request.POST['username'])
    return render(request, 'adduser.html')


# def Rank(request):
#     aaa = BeerPongRankingTable.objects.order_by('-wins')
#     for i in range(1, len(aaa) + 1):
#         aaa[i - 1].rank = i
#         aaa[i - 1].save()
#         print('aaa[i].wins', aaa[i-1].wins, type(aaa))
    
#     context2 = {'fff': aaa}

#     return render(request, 'rank.html', context2)