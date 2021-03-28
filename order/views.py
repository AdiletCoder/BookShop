from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from .forms import CreateOrderForm
from .models import Order
from main.models import Book

def create_order(request, book_id):
    book = Book.objects.get(id=book_id)
    print(request.POST)
    order_form = CreateOrderForm(request.POST)
    if order_form.is_valid():
        print(order_form.cleaned_data)
        # order = Order.objects.create(**order_form.cleaned_data)
        order_form.save()
        return redirect(book.get_absolute_url)
    order_form = CreateOrderForm()
    return render(request, 'order/order.html', {'form': order_form, 'book': book})





