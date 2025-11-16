from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import products
from django.contrib.auth import get_user_model




class ProductDetailView(DetailView):
    model = products
    template_name = "product_details.html"
    context_object_name = "product"
    
    #User = get_user_model()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_user'] = get_user_model()
        return context







