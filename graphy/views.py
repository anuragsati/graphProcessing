from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Graph
from django.conf import settings
from .forms import GraphForm

from pyvis.network import Network
net = Network(height='600px', width='800px')
net.toggle_physics(False)

def save_graph():
    data = Graph.objects.all()

    for p in data:
        net.add_node(p.startNode, label=str(p.startNode))
        net.add_node(p.endNode, label=str(p.endNode))

    for p in data:
        net.add_edge(p.startNode, p.endNode)
    
    net.save_graph(str(settings.BASE_DIR) + '/graphy/templates/pvis_graph_file.html')


def index(request):
    if request.method == 'POST':
        if request.POST['startNode'] and request.POST['endNode']:
            form = GraphForm(request.POST)
            form.save()

    save_graph()
    return render(request, 'index.html', {'isEmpty' : False})

def clearGraph(request):
    Graph.objects.all().delete()
    save_graph()
    return render(request, 'index.html', {'isEmpty' : True})
