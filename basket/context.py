from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery_total = 0
    basket = request.session.get('basket', {})
    
    if basket != {}:
        for item in basket['items']:
            print(item)
            print(item['item_id'])
            product = get_object_or_404(Product, pk=item['item_id'])
            print(product)
            print("product price")
            print(product.price)
            print(type(product.price))
            print(item['quantity'])
            print(type(item['quantity']))

            # You were dealing with the delivery
            subtotal = item['quantity'] * product.price
            digital_download = "Delivery"
            if item['digital_download']:
                digital_download = "Yes"
            else:
                digital_download = "Delivery"
                delivery_total += subtotal

            total += subtotal

            basket_items.append({
                'item': item,
                'product': product,
                'subtotal': subtotal,
                'digital_download': digital_download,
                
            })
        print("basket_items")
        print(basket_items)
        # for item_id, item_data in basket.items():
        #     if isinstance(item_data, int):
        #         product = get_object_or_404(Product, pk=item_id)
        #         total += item_data * product.price
        #         product_count += item_data
        #         basket_items.append({
        #             'item_id': item_id,
        #             'quantity': item_data,
        #             'product': product,
        #             })
        #     else:
        #         product = get_object_or_404(Product, pk=item_id)
        #         for digital_download, quantity in item_data['items_by_download_choice'].items():
        #             total += quantity * product.price
        #             product_count += quantity
        #             basket_items.append({
        #                 'item_id': item_id,
        #                 'quantity': item_data,
        #                 'product': product,

        #             })
   

    if delivery_total == 0 or total > settings.FREE_DELIVERY_AMOUNT:
        print(delivery_total)
        print(total)
        delivery = 0
        free_delivery_deficit = 0
    else:
        delivery = Decimal.from_float(settings.STANDARD_DELIVERY_AMOUNT)
        free_delivery_deficit = settings.FREE_DELIVERY_AMOUNT - total
    
    
    grand_total = delivery + total
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_deficit': free_delivery_deficit,
        'FREE_DELIVERY_AMOUNT': settings.FREE_DELIVERY_AMOUNT,
        'grand_total': grand_total,
        'new_customer_offer': settings.NEW_CUSTOMER_OFFER,
        'delivery_total': delivery_total
      
    }

    return context
