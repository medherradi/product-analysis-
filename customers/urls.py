from django.urls import path
from .views import corr_customer

app_name = 'customers'

urlpatterns = [
    path('', corr_customer, name='customer_insight')
]
