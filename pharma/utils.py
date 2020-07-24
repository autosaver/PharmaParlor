import json
from . models import *


def cookieCart(request):
    try:
        # parses the cookie and turns it into a python dictionary
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}  # to prevent key error when cookie cart is deleted

    print('Cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']

    # displays cart items in nav bar
    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            # cart total price plus price of an items's quantity when added to cart
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            # displays items of Anonymous user and stores in cookie
            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    # 'imageURL':product.imageURL
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }
            items.append(item)

            if product.stock >= 1:
                order['shipping'] = True
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items': items}
