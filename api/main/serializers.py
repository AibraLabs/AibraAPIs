from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import *



class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        # fields = ('id', 'title', 'description', 'completed')
        # Shortcut for getting all fields
        fields = '__all__'



class BalanceSerializer(serializers.Serializer):
    balance = serializers.CharField(max_length=120)
    class Meta:
        #model = Wallet
        fields = ('balance')



class TxnSerializer(serializers.Serializer):
    tx_hash = serializers.CharField(max_length=120)
    class Meta:
        #model = Wallet
        fields = ('tx_hash')
