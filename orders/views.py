from django.contrib.auth.models import User

def create_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@gmail.com', 'admin123')
    return HttpResponse("Admin created")
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Order
from products.models import Product

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_detail')

    items = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * quantity
        total += subtotal
        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone = request.POST.get('phone')

        Order.objects.create(
            full_name=full_name,
            address=address,
            city=city,
            phone=phone,
            total_amount=total
        )

        request.session['cart'] = {}
        return render(request, 'order_success.html')

    return render(request, 'checkout.html', {
        'items': items,
        'total': total
    })
