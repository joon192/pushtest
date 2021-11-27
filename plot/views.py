from django.shortcuts import render

# Create your views here.

from plot.function import make_df, make_bar_plot



def graph(request):
     total = make_df()
     make_bar_plot(total)
     return render(request, 'plot/graph.html')
