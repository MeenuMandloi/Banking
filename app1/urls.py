from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('bankindex/', views.bankindex,name="bankindex"),
    path('bankcreate/', views.bankcreate,name="bankcreate"),
    path('logout/', views.logout,name="logout"),
    path('banklogin/', views.banklogin,name="banklogin"),
    path('CreateAccount/', views.CreateAccount,name="CreateAccount"),
    path('TransferMoney/',views.TransferMoney,name="TransferMoney"),
    path('BalanceEnquiry/',views.BalanceEnquiry,name="BalanceEnquiry"),
    path('TransectionDetails/',views.TransectionDetails,name="TransectionDetails"),
    path('Withdrawl/',views.Withdrawl,name="Withdrawl"),
    path('ViewProfile/',views.ViewProfile,name="ViewProfile"),
    path('Deposite/',views.Deposite,name="Deposite"),

]
