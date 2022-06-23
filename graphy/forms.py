from dataclasses import fields
from django import forms
from .models import Graph

class GraphForm(forms.ModelForm):
    class Meta:
        model = Graph
        fields = ['startNode', 'endNode']