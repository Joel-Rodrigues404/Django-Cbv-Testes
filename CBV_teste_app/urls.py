from django.urls import path
from django.views.generic import TemplateView
from CBV_teste_app.views import TempView, ProdutosList



urlpatterns = [
    path(
        'template_view/', 
        TemplateView.as_view(template_name='CBV_teste_app/template_view.html'), 
        name='template-view'),
    path(
        'tempview/', TempView.as_view(), name='temp-view'
        ),
    path(
        'cbv/', ProdutosList.as_view(), name='cbv'
    ),
]
