from django.views.generic import DetailView, ListView
from .models import products
from reviews.models import Review
import json
from django.contrib.auth import get_user_model
User = get_user_model()

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
        context['reviews'] = Review.objects.filter( #TODO this line might need to be fixed 
            product_id=self.get_object()
        ).order_by('-review_id')

        current_user_id = self.request.user.id
        current_user = User.objects.get(id=current_user_id)
        print("type(current_user)---------------------")
        print(type(current_user))

        print("type(current_user.user_owned_products)---------------------")
        print(type(current_user.user_owned_products))

        
        test = current_user.user_owned_products.products.all()
        
        print(test)
        owned_books = current_user.user_owned_products.products

        for item in owned_books.all():
            print(item)

        context['jsinfo'] = json.dumps({'product_id':self.get_object().product_id,
                                        'user_id':self.request.user.id,
                                        'all_books':self.request.user.user_owned_books}) #sends json info to be used by js of user info
        return context







