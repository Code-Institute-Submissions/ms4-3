def processing_linked_products(request, item_id):

    product = get_object_or_404(Product, pk=item_id)

    if product.number_of_pictures > 0:
        # read each value from the form
        number_of_products_to_link = product.number_of_pictures

        linked_product_images_list = []

        # Splitting the linked_products meta-data and appending them to the arrays above.
        for i in range(number_of_products_to_link):
            linked_product_details = request.POST.get('linked_product' + str(i))
            split_linked_product_details = linked_product_details.split("|")

            linked_product_id = split_linked_product_details[1]
            linked_product_image = split_linked_product_details[0]
            linked_product_type = split_linked_product_details[2]

            # If it is an uploaded picture, query the database for it.
            if linked_product_type == 'upload':
                linked_product_object = get_object_or_404(Image_upload, pk=linked_product_id)

            # This process the different paths needed to display the linked images of each product in basket.
            if linked_product_images_list != []:
                if linked_product_type == "upload":
                    linked_product_image = "/media/" + linked_product_image
                    linked_product_images_list.append(linked_product_image)
                else:
                    linked_product_images_list.append(linked_product_image)
            else:
                if linked_product_type == "upload":
                    linked_product_image = "/media/" + linked_product_image
                    linked_product_images_list.insert(0, linked_product_image)
                else:
                    linked_product_images_list.insert(0, linked_product_image)
    else:
        linked_product_images_list = ['Not available']
    linked_product_images_list = linked_product_images_list()
    return linked_product_images_list




def processing_linked_products_for_checkout_summary(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    linked_products = []
    
    if product.number_of_pictures > 0:
        # read each value from the form
        number_of_products_to_link = product.number_of_pictures
      # Splitting the linked_products meta-data and appending them to the arrays above.
        for i in range(number_of_products_to_link):
            linked_product_details = request.POST.get('linked_product' + str(i))
            split_linked_product_details = linked_product_details.split("|")
            linked_product_id = split_linked_product_details[1]
            linked_product_image = split_linked_product_details[0]
            linked_product_type = split_linked_product_details[2] 


            # This stores the different SKU in an array for the order summary.
            if linked_product_id == "No id":
                if linked_products != []:
                    linked_products.append('Not linked')
                else:
                    linked_products.insert(0, 'Not linked')
            elif linked_product_type == 'upload':
                if linked_products != []:
                    linked_products.append(str(linked_product_object.sku))
                else:
                    linked_products.insert(0, str(linked_product_object.sku))
            else:
                linked_product = get_object_or_404(Product, pk=linked_product_id)
                if linked_products != []:
                    linked_products.append(linked_product.sku)
                else:
                    linked_products.insert(0, linked_product.sku)   
    else:
        linked_products = ['Not available']
    linked_products = linked_products()
    return linked_products









def add_to_basket(request, item_id):
    # Requesting basket information
    basket = request.session.get('basket', {})
    basket_item_id = request.session.get('basket_item_id')

    # Retrieving form data
    quantity = int(request.POST.get('quantity'))
    digital_download = request.POST.get('digital_download')
    linked_products = [['Not linked']]  # Default setting
    product = get_object_or_404(Product, pk=item_id)
    # Item id is passed through as parameter to identify the linked product.
    processing_linked_products(request, item_id)
    processing_linked_products_for_checkout_summary(request, item_id)
     

    # checking to see if any of the linked products has repeated pictures to give the user a warning.
    repeats_found = 'None'
    if product.number_of_pictures > 1:
        for i in range(0, len(linked_products)):
            for j in range(i+1, len(linked_products)):
                if linked_products[i] == linked_products[j]:
                    if linked_products[i] != "Not linked":
                        repeats_found = 'There are repeated pictures in your product.'

    # appending the items to the basket
    if basket != {}:
        for item in basket['items']:
            basket_item_id = basket_item_id + 1

        #This next function decides whether the product already exists in the basket. 
        matching_items = []
        if linked_products[0] == "Not available":
            for item in basket['items']:
                # If the ID is in and the the digi-download is on OR off and matches it goes through here.
                if item_id == item['item_id'] and digital_download == item['digital_download']:
                    matching_items.append(item)
        else:
            for item in basket['items']:
                if item_id == item['item_id'] and linked_products == item['linked_products']:
                    matching_items.append(item)

        # This next section will either update an basket item quantity or append a new item.
        if matching_items:
            if matching_items[0]['item_id'] == item_id:
                matching_items[0]['quantity'] += quantity
        else:
            basket['items'].append({
                'basket_item_id': basket_item_id,
                'item_id': item_id,
                'digital_download': digital_download,
                'quantity': quantity,
                'linked_products': linked_products,
                'linked_product_images_list': linked_product_images_list,
                'repeats_found': repeats_found
            })
    else:
        basket['items'] = []
        request.session['basket_item_id'] = 1
        basket['items'].append({
            'basket_item_id': 1,
            'item_id': item_id,
            'digital_download': digital_download,
            'quantity': quantity,
            'linked_products': linked_products,
            'linked_product_images_list': linked_product_images_list,
            'repeats_found': repeats_found
        })

    redirect_url = request.POST.get('redirect_url')
    request.session['basket'] = basket
    messages.success(request, f"Successfully added '{product.friendly_name}' to your basket.")
    return redirect(redirect_url)





''' This add_to_basket function will add a product to the basket. It receive the information from a form,
    store the information in a json and then save the basket.
    It has several feature checks along the way: type of delivery, any linked products?,
    checking for duplicated linked products. Linked products are photographs that can
    be added to a container purchase.'''


def add_to_basket(request, item_id):
    # Requesting basket information
    basket = request.session.get('basket', {})
    basket_item_id = request.session.get('basket_item_id')

    # Retrieving form data
    quantity = int(request.POST.get('quantity'))
    digital_download = request.POST.get('digital_download')
    linked_products = [['Not linked']]

    # Item id is passed through as parameter to identify the linked product.
    product = get_object_or_404(Product, pk=item_id)

    if product.number_of_pictures > 0:
        # read each value from the form
        number_of_products_to_link = product.number_of_pictures

        linked_products = []
        linked_product_images_list = []

        # Splitting the linked_products meta-data and appending them to the arrays above.
        for i in range(number_of_products_to_link):
            linked_product_details = request.POST.get('linked_product' + str(i))
            split_linked_product_details = linked_product_details.split("|")

            linked_product_id = split_linked_product_details[1]
            linked_product_image = split_linked_product_details[0]
            linked_product_type = split_linked_product_details[2]

            # If it is an uploaded picture, query the database for it.
            if linked_product_type == 'upload':
                linked_product_object = get_object_or_404(Image_upload, pk=linked_product_id)

            # This process the different paths needed to display the linked images of each product in basket.
            if linked_product_images_list != []:
                if linked_product_type == "upload":
                    linked_product_image = "/media/" + linked_product_image
                    linked_product_images_list.append(linked_product_image)
                else:
                    linked_product_images_list.append(linked_product_image)
            else:
                if linked_product_type == "upload":
                    linked_product_image = "/media/" + linked_product_image
                    linked_product_images_list.insert(0, linked_product_image)
                else:
                    linked_product_images_list.insert(0, linked_product_image)

            # This stores the different SKU in an array for the order summary.
            if linked_product_id == "No id":
                if linked_products != []:
                    linked_products.append('Not linked')
                else:
                    linked_products.insert(0, 'Not linked')
            elif linked_product_type == 'upload':
                if linked_products != []:
                    linked_products.append(str(linked_product_object.sku))
                else:
                    linked_products.insert(0, str(linked_product_object.sku))
            else:
                linked_product = get_object_or_404(Product, pk=linked_product_id)
                if linked_products != []:
                    linked_products.append(linked_product.sku)
                else:
                    linked_products.insert(0, linked_product.sku)
    else:
        linked_products = ['Not available']
        linked_product_images_list = ['Not available']

    # checking to see if any of the linked products has repeated pictures to give the user a warning.
    repeats_found = 'None'
    if product.number_of_pictures > 1:
        for i in range(0, len(linked_products)):
            for j in range(i+1, len(linked_products)):
                if linked_products[i] == linked_products[j]:
                    if linked_products[i] != "Not linked":
                        repeats_found = 'There are repeated pictures in your product.'

    # appending the items to the basket
    if basket != {}:
        for item in basket['items']:
            basket_item_id = basket_item_id + 1

        #This next function decides whether the product already exists in the basket. 
        matching_items = []
        if linked_products[0] == "Not available":
            for item in basket['items']:
                # If the ID is in and the the digi-download is on OR off and matches it goes through here.
                if item_id == item['item_id'] and digital_download == item['digital_download']:
                    matching_items.append(item)
        else:
            for item in basket['items']:
                if item_id == item['item_id'] and linked_products == item['linked_products']:
                    matching_items.append(item)

        # This next section will either update an basket item quantity or append a new item.
        if matching_items:
            if matching_items[0]['item_id'] == item_id:
                matching_items[0]['quantity'] += quantity
        else:
            basket['items'].append({
                'basket_item_id': basket_item_id,
                'item_id': item_id,
                'digital_download': digital_download,
                'quantity': quantity,
                'linked_products': linked_products,
                'linked_product_images_list': linked_product_images_list,
                'repeats_found': repeats_found
            })
    else:
        basket['items'] = []
        request.session['basket_item_id'] = 1
        basket['items'].append({
            'basket_item_id': 1,
            'item_id': item_id,
            'digital_download': digital_download,
            'quantity': quantity,
            'linked_products': linked_products,
            'linked_product_images_list': linked_product_images_list,
            'repeats_found': repeats_found
        })

    redirect_url = request.POST.get('redirect_url')
    request.session['basket'] = basket
    messages.success(request, f"Successfully added '{product.friendly_name}' to your basket.")
    return redirect(redirect_url)