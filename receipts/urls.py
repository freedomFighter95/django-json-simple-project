from django.urls import path
from receipts import views
urlpatterns = [
    path('receipt_jason/', views.receipt_jason)   
]

