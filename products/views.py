from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import products
from accounts.models import base_user




class ProductDetailView(DetailView):
    template_name = "product_details.html"
    model = products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_user'] = base_user.objects.all()
        return context






