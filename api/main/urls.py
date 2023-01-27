from django.urls import path
from . import views

app_name = "main"


from . import views
from rest_framework import routers
from django.urls import path, include


urlpatterns = [


    #crypto api
    
    
    #######brise ns shitttttt
    path('bns/get-address/<str:name>/', views.GetAddressView),
    path('bns/get-name/<str:address>/', views.GetNameView),
    path('bns/get-price/<str:name>/', views.GetPriceView),
    path('bns/withdraw/', views.WithdrawView),
    path('bns/transfer/<int:name>/<str:address_from>/<str:address_to>/', views.TransferView),
    path('bns/get-detail/', views.GetDetailView),
    
    
    
    #########brise shit modafuckers
    path('aibra/get-balance/<str:wallet_address>/', views.AibraGetBalanceView),
    path('brise-get-balance/<str:wallet_address>/', views.BriseGetBalanceView),
    path('brise-create-wallet/', views.BriseCreateWallet),
    path('send-brise/', views.SendBrise),
    
    
    
    #bitrise
    path('bitgert/get-balance/<str:wallet_address>/', views.BitgertGetBalanceView),
    path('bitrise-get-balance/<str:wallet_address>/', views.BitriseGetBalanceView),
    path('bitrise-create-wallet/', views.BitriseCreateWallet),
    path('send-bitrise/', views.SendBitrise),
    
    
    

    
    #ok
    path('okx/get-balance/<str:wallet_address>/', views.OKGetBalanceView),
    path('okx-get-balance/<str:wallet_address>/', views.OKxGetBalanceView),
    path('okx-create-wallet/', views.OKxCreateWallet),
    path('send-okx/', views.SendOKx),




]

