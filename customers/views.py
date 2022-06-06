from pickle import NONE
from django.shortcuts import render
import pandas as pd
from plotly.offline import plot 
import plotly.express as px
from .models import Customer
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def corr_customer(request):
      success_message = None
      error_message = None
      corr = None
      fig = None
      graph_plot = None
      query_set = Customer.objects.all()
      customer_df = pd.DataFrame(query_set.values())
      if customer_df.shape[0] > 0:
            corr = round(customer_df['budget'].corr(customer_df['employment']),2)
            fig = px.scatter(customer_df, x='budget', y='employment',
                        marginal_x='histogram', marginal_y='histogram',
                        color='budget',
                        title ='relation between employment and budget in morrocan company'
                        )
            graph_plot = plot(fig, output_type="div")
            success_message = 'customers data displayed successfully'
      else: 
            error_message = 'no data to display'
      context = {
            'success_message': success_message,
            'error_message': error_message,
            'corr': corr,
            'graph_plot': graph_plot
      }
      return render(request, 'customers/main.html', context)