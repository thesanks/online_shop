from django.views.generic import ListView
from django.shortcuts import render

from .models import Product


# just trying out class and function based views
# overwriting default templates etc
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # writing get_context_data...what's returned?
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data( *args, **kwargs)
    #     print(context)
    #     return context

def product_list_view(request):
    queryset = Product.objects.all()
    return render(request, 'products/list.html', {'object_list': queryset})
