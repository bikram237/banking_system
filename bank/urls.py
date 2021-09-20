from django.urls import path
from . import views
urlpatterns = [
    path("", views.HomePage, name="home" ),

    path("transfer/<int:id>/", views.TransferPage, name="Transfer"),
    path("deposit/<int:id>/", views.DepositPage, name="Deposit"),
    path("withdraw/<int:id>/", views.WithdrawPage, name="Withdraw"),
    path("history/", views.HistoryPage, name="History"),
    path("users/", views.UsersPage, name="Users"),
    

    

]