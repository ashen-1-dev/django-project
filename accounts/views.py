from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import CustomUserCreationForm
from orders.models import OrderItem


# from accounts.forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required(login_url='/accounts/login/')
def order_history(request):
    user = request.user
    orders = OrderItem.objects.filter(order__first_name__exact=user.first_name, order__last_name__exact=user.last_name)
    return render(request, 'order_history.html', {'orders': orders})