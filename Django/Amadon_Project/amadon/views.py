from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def viewOrder(request):
    order_id = request.session["total_charge"]
    sum1 = 0
    sum2 = 0
    for order in Order.objects.all():
        sum1 += order.quantity_ordered
        sum2 += order.total_price
    context = {
        "order" : Order.objects.get(id=order_id),
        "total_order" : sum1,
        "total_price" : sum2
    }
    return render(request, "checkout.html", context)

def checkout(request):
    product_id = request.POST["product_id"]
    request.session["productId"] = product_id
    quantity_from_form = int(request.POST["quantity"])
    this_product = Product.objects.get(id=product_id)
    total_charge = quantity_from_form * this_product.price
    print("Charging credit card...")
    this_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    request.session["total_charge"] = this_order.id
    return redirect("/checkout/view")