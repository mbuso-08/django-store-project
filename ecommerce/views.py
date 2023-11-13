from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .models import Item, OrderItem, Order
from django.contrib.auth.decorators import login_required

# Create your views here.

class HomeView(ListView):
    model = Item
    template_name = "home.html"

# def item_list(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, 'item-list.html', context)

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'product.html', context)

class ItemDetailView(DetailView):
    http_method_names = ['get']
    model = Item
    template_name = "product.html"
    context_object_name = "product"

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        ordered=False,
        user=request.user
        )
    order_qs = Order.objects.filter(user=request.user, ordered= False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user,
                                     order_date=order_date)
        order.items.add(order_item)
    return redirect("ecommerce:product", slug=slug)

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
        item=item,
        ordered=False,
        user=request.user
        )[0]
            order.items.remove(order_item)
        else:
            return redirect("ecommerce:product", slug=slug)
    else:
        return redirect("ecommerce:product", slug=slug)
    return redirect("ecommerce:product", slug=slug)


@login_required
def show_cart(request, *args, **kwargs):
    user = request.user
    try:
        cart = Order.objects.get( ordered=False)
        # cart = Order.objects.filter(user=user)
        context = {
            'object': cart
        }
        amount = 0
        for item in cart:
            value = item.quantity * item.price
            amount = amount + value
            total_price = amount + 90
        return render(request, 'cart.html', context)
    except ObjectDoesNotExist:
        messages.error(request, "You do not have an active order")
        return redirect("/")

