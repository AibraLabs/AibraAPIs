from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
from .RayBnb import *
from .RayBitgert import *
from .RayBitrise import *
from .RayOkx import *
from .RayBns import GetBnsAddress, GetBnsPrice, GetBnsName, Withdraw, Transfer, GetDetail


@api_view(['POST'])
def WalletView(request):

    if request.method == 'POST':

        wallet = CreateWallet()

        data = {
        "username": request.data["username"],
        "public_key": wallet["wallet_address"],
        "private_key": wallet["wallet_key"],

        }

        #return HttpResponse(str(request.data))

        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def GetBnbBalanceView(request, wallet_address):

    if request.method == 'GET':
        balance = GetBalance(wallet_address, "ether")

        data = {
        "balance": str(balance),
        }

        #return HttpResponse(str(data))

        serializer = BalanceSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)

        else:
            return HttpResponse(str("errors!"))




#########brise ns shittttttt
@api_view(['GET'])
def GetAddressView(request, name):

    if request.method == 'GET':
        address = GetBnsAddress(name)

        data = {
        "address": str(address),
        }

        return Response(data)

@api_view(['GET'])
def GetNameView(request, address):

    if request.method == 'GET':
        name = GetBnsName(address)

        data = {
        "names": (name),
        }

        return Response(data)

@api_view(['GET'])
def GetPriceView(request, name):

    if request.method == 'GET':
        price = GetBnsPrice(name)

        data = {
        "price": str(price),
        }

        return Response(data)

@api_view(['GET'])
def WithdrawView(request):

    if request.method == 'GET':
        result = Withdraw()

        data = {
        "result": str(result),
        }

        return Response(data)
        
        
@api_view(['GET'])
def TransferView(request, name, address_from, address_to):

    if request.method == 'GET':
        result = Transfer(name, address_from, address_to)

        data = {
        "result": str(result),
        }

        return Response(data)
     
@api_view(['GET'])
def GetDetailView(request):

    if request.method == 'GET':
        result = GetDetail()

        data = {
        "result": str(result),
        }

        return Response(data)   

##########brise shit modafurkers
@api_view(['POST'])
def BriseCreateWallet(request):

    if request.method == 'POST':

        wallet = BCreateWallet()

        data = {
        "username": request.data["username"],
        "public_key": wallet["wallet_address"],
        "private_key": wallet["wallet_key"],

        }

        #return HttpResponse(str(request.data))

        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def BriseGetBalanceView(request, wallet_address):
    if request.method == 'GET':
        balance = GetAltBalance(wallet_address)

        data = {
        "data": balance,
        }


        return Response(data)


@api_view(['GET'])
def AibraGetBalanceView(request, wallet_address):
    if request.method == 'GET':
        balance = GetAibraBalance(wallet_address)

        data = {
        "data": balance,
        }


        return Response(data)
        

@api_view(['POST'])
def SendBrise(request):

    if request.method == 'POST':
        sender = request.data["sender"]
        receiver = request.data["receiver"]
        amount = request.data["amount"]
        sender_key = request.data["sender_key"]
        token = request.data["token"]

        txn_hash = SendB(sender, sender_key, receiver, amount, token)

        data = {
        "txn_hash": str(txn_hash),

        }

        return Response(data)
        
        
        
        
##########bitrise shit modafurkers
@api_view(['POST'])
def BitriseCreateWallet(request):

    if request.method == 'POST':

        wallet = BBCreateWallet()

        data = {
        "username": request.data["username"],
        "public_key": wallet["wallet_address"],
        "private_key": wallet["wallet_key"],

        }

        #return HttpResponse(str(request.data))

        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def BitriseGetBalanceView(request, wallet_address):
    if request.method == 'GET':
        balance = GetAlterBalance(wallet_address)

        data = {
        "data": balance,
        }


        return Response(data)


@api_view(['GET'])
def BitgertGetBalanceView(request, wallet_address):
    if request.method == 'GET':
        balance = GetBitgertBalance(wallet_address)

        data = {
        "data": balance,
        }


        return Response(data)
        

@api_view(['POST'])
def SendBitrise(request):

    if request.method == 'POST':
        sender = request.data["sender"]
        receiver = request.data["receiver"]
        amount = request.data["amount"]
        sender_key = request.data["sender_key"]
        token = request.data["token"]

        txn_hash = SendBB(sender, sender_key, receiver, amount, token)

        data = {
        "txn_hash": str(txn_hash),

        }

        return Response(data)
        
        
##########okchain shit modafurkers
@api_view(['POST'])
def OKxCreateWallet(request):

    if request.method == 'POST':

        wallet = OKCreateWallet()

        data = {
        "username": request.data["username"],
        "public_key": wallet["wallet_address"],
        "private_key": wallet["wallet_key"],

        }

        #return HttpResponse(str(request.data))

        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def OKxGetBalanceView(request, wallet_address):
    if request.method == 'GET':
        balance = GetAlterOKBalance(wallet_address)

        data = {
        "data": balance,
        }


        return Response(data)


@api_view(['GET'])
def OKGetBalanceView(request, wallet_address):
    if request.method == 'GET':
        balance = GetOKBalance(wallet_address)

        data = {
        "data": balance,
        }


        return Response(data)
        

@api_view(['POST'])
def SendOKx(request):

    if request.method == 'POST':
        sender = request.data["sender"]
        receiver = request.data["receiver"]
        amount = request.data["amount"]
        sender_key = request.data["sender_key"]
        token = request.data["token"]

        txn_hash = SendOK(sender, sender_key, receiver, amount, token)

        data = {
        "txn_hash": str(txn_hash),

        }

        return Response(data)
