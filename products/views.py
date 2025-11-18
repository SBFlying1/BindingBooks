from django.views.generic import DetailView, ListView
from .models import products, product_review


class ProductListView(ListView):
    model = products
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = products
    template_name = "product_details.html"
    context_object_name = "product"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = product_review.objects.filter(
            product_being_reviewed=self.get_object()
        ).order_by('-post_id')
        return context







