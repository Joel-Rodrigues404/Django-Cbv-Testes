from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import Produtos
# Create your views here.


class TempView(TemplateView):
    template_name = 'CBV_teste_app/temp_view.html'

class ProdutosList(ListView):
    model = Produtos
    queryset = Produtos.objects.all()