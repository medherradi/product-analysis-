from django.urls import path
from .views import (chart_select_view, 
                    add_purchase_view,
                    salesman_performance,
                    home_view,
                    )

app_name='analysis'

urlpatterns = [
    path('', home_view, name='home-view'),
    path('analysis/', chart_select_view, name='main-view'),
    path('add-purchase/', add_purchase_view, name='add-view'),
    path('salesman/', salesman_performance, name='sales_view'),
]
