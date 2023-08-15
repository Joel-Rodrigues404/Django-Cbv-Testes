from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView, DeleteView, View
)
from .models import Cliente

# Create your views here.

#procura numa pasta com nome da app um arquivo com nome modelo + _list.html no caso seria cliente_list.html
class ClienteList(ListView):
    model = Cliente
    paginate_by = 1
    queryset = Cliente.objects.all()

#procura numa pasta com nome da app um arquivo com nome modelo + _form.html no caso seria cliente_form.html
class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')

#usa o mesmo html de ClienteCreate pois todos os valores são iguais
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')

#procura numa pasta com nome da app um arquivo com nome modelo + _detail.html no caso seria cliente_detail.html
class ClienteDetail(DetailView):
    queryset = Cliente.objects.all()


class ClienteDelete(DeleteView):
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('exemplo:list')

class Viewwww(View):
    return ...
