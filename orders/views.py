from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created



@login_required(login_url='/accounts/login/')
def order_create(request):
  cart = Cart(request)
  if request.method == 'POST':
    form = OrderCreateForm(request.POST)
    if form.is_valid():
      order = form.save()
      for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
      cart.clear()
      order_created.delay(order.id)
  else:
    user = request.user
    form = OrderCreateForm(initial={"first_name": user.first_name, "last_name": user.last_name, "email": user.email})

  return render(request, 'orders/create.html', {'cart': cart, 'form': form})
