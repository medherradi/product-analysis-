from django.shortcuts import render
from .models import Product, Purchase 
import pandas as pd
from plotly.offline import plot 
import plotly.express as px
from .forms import PurchaseForm
from django.http import HttpResponse
from .utils import get_salesman_name
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
      return render(request, 'analysis/home.html', {})


@login_required
def chart_select_view(request):
      error_message = None
      #graph = None
      data_date = None
      data_product = None
      graph_plot = None
      fig = None
      query_set_product = Product.objects.all()
      query_set_purchase = Purchase.objects.all()
      purchase_data = [
            {
                  'id': x.id,
                  'product_name': x.product.name,
                  'quantity': x.quantity,
                  'total_price': x.total_price,
                  'salesman': x.salesman,
                  'date': x.date
            } for x in query_set_purchase
      ]
      purchase_df = pd.DataFrame(purchase_data)
      if purchase_df.shape[0] > 0:
            if request.method == 'POST':
                  chart_type = request.POST.get('choices')
                  date_from = request.POST.get('date-from')
                  date_to = request.POST.get('date-to')  
                  purchase_df['date'] = purchase_df['date'].apply(lambda x : x.strftime('%Y-%m-%d'))
                  purchase_df = purchase_df[(purchase_df['date'] > date_from) & (purchase_df['date'] < date_to)]
                  data_date = purchase_df.groupby('date', as_index=False)['total_price'].agg('sum')
                  data_product = purchase_df.groupby('product_name', as_index=False)['total_price'].agg('sum') 
                  if data_product.shape[0] > 0 and data_date.shape[0] > 0:
                        if chart_type == 'pie plot':
                              if date_from != "" and date_to != "":
                                    fig = px.pie(data_product, values='total_price', names='product_name',title='Product total price pie chart') 
                                    graph_plot = plot(fig, output_type="div")
                        elif chart_type == 'line plot': 
                              if date_from != "" and date_to !="":    
                                    fig = px.line(data_date, x='date', y='total_price',title='Product total price line chart')
                                    graph_plot = plot(fig, output_type="div")
                        elif chart_type == 'bar plot':   
                              if date_from != "" and date_to !="":    
                                    fig = px.bar(data_product, x='product_name', y='total_price',title='Product total price bar plot')
                                    graph_plot = plot(fig, output_type="div")
                        else: 
                              error_message = 'Please select a chart type to display the graph'
                  else:
                        error_message = 'no data to display'
      else: 
            error_message = 'no data to display'
      context = {
            'error_message': error_message,
            'qs_product': query_set_product,
            'qs_purchase': query_set_purchase,
            'graph_plot': graph_plot
            }
      return render(request, 'analysis/main.html', context)

@login_required
def add_purchase_view(request):
      form = PurchaseForm(request.POST or None)
      message = None
      if form.is_valid():
            obj = form.save(commit=False)
            print(obj)
            obj.salesman = request.user
            obj.save()
            form = PurchaseForm()
            message = f'The product {obj.product.name} with a quantity of {obj.quantity} has been sold'
      context={
            'form': form,
            'message': message,
      }
      return render(request, 'analysis/add.html', context)

@login_required
def salesman_performance(request):
      query_set = Purchase.objects.all()
      purchase_df = pd.DataFrame(query_set.values())
      purchase_df['salesman_id'] = purchase_df['salesman_id'].apply(get_salesman_name)
      purchase_df.rename({'salesman_id':'salesman'}, axis=1, inplace=True)
      purchase_df['date'] = purchase_df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
      #print(purchase_df['date'])
      fig = px.bar(purchase_df, x='date', y='total_price', color='salesman',title='Salesman purchase total price bar plot')
      graph_plot = plot(fig, output_type="div")
      context= {
            'graph_plot': graph_plot
      }
      return render(request, 'analysis/sale-performance.html', context)











