from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from products.models import Product
from comments.forms import CommentForm
from django.views.generic.list import ListView
import stripe
from django.conf import settings
from django.http import HttpResponse
class HomeView(TemplateView):
    template_name="products/home.html"
    def get_context_data(self,*args,**kwargs):
        products = Product.objects.all()
        return{'products':products}

class ProductDetailView(DetailView):
    model = Product
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        comment_form=CommentForm()
        context['comment_form'] = comment_form
        return context

def search_product(request):
    query = request.GET.get('query','')
    product = Product.objects.filter(title__icontains = query)
    return render(request,"products/search_product.html",{'product':product})

class ProductByCategory(TemplateView):
    template_name="products/products_by_category.html"
    model = Product
    def get_context_data(self,*args,**kwargs):
        query = kwargs['query']
        products = Product.objects.all()
        return {
        'query':query,
        'products':products
        }



class ProductBuyView(DetailView):
    model = Product
    template_name = 'products/buy.html'
    def post(self,request,*args, **kwargs):
        stripe.api_key = settings.STRIPE_API_KEY
        token = request.POST['stripeToken']
        product = self.get_object()
        charge = stripe.Charge.create(
            amount = product.price * 100,
            currency = 'USD',
            description = 'cobro por {}'.format(product.title),
            statement_descriptor = "cobro de compusur",
            source = token
        )
        return render(request, "products/success.html", {'debug_info':charge, 'product':product})
