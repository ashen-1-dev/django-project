from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView, FormView

from cart.forms import CartAddProductForm
from shop.models import Product
import _logger


class HomeView(TemplateView):
    template_name = 'shop/home.html'


class ProductListView(ListView):
    model = Product
    template_name = 'shop/list.html'
    context_object_name = 'all_products'


class CategoryView(ListView):
    model = Product
    template_name = 'shop/list.html'
    context_object_name = 'all_products'

    def get_queryset(self, **kwargs):
        _logger.logger.debug(self.kwargs)
        category_slug = self.kwargs['category_slug']
        _logger.logger.debug(category_slug)
        products = Product.objects.filter(category__slug__icontains=category_slug)
        _logger.logger.debug(products)
        return products


class BrandView(ListView):
    model = Product
    template_name = 'shop/list.html'
    context_object_name = 'all_products'

    def get_queryset(self, **kwargs):
        _logger.logger.debug(self.kwargs)
        brand_slug = self.kwargs['brand_slug']
        _logger.logger.debug(brand_slug)
        products = Product.objects.filter(brand__slug__icontains=brand_slug)
        _logger.logger.debug(products)
        return products

class ProductDetail(DetailView, FormView):
  model = Product
  form_class = CartAddProductForm
  template_name = 'shop/detail.html'

  def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail.html', {'product': product, 'cart_product_form': cart_product_form})