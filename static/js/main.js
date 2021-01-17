 $('#addToBasket').click(function(){
        item = sessionStorage.getItem('currentBasketAmount')
        if (item == null){
            sessionStorage.setItem('currentBasketAmount', 0);
             sessionStorage.setItem('newBasketAmount', 1);
        } else{
            item++;
            sessionStorage.setItem('newBasketAmount', item)
        }
        console.log(item);
 });

$('#emptyBasket').click(function(){
    sessionStorage.clear();
    console.log("should clear");
});


$( document ).ready(function() {
    console.log( "ready!" );

 
     $("#desktopExtraNavWrapper").hover(function(){
        $("#desktopDropDownMenu").css('display', 'flex');}
        ,function(){
    $("#desktopDropDownMenu").css('display', 'none');
    });

    // $("#id_discount_price").addClass('hide');
    
    let currentBasketAmount = sessionStorage.getItem('currentBasketAmount')
    let newBasketAmount = sessionStorage.getItem('newBasketAmount')
    console.log(currentBasketAmount)
    console.log(newBasketAmount)
    if(newBasketAmount > currentBasketAmount){
        $(".fa-shopping-basket").addClass('item-added-transition');
        sessionStorage.setItem('currentBasketAmount', newBasketAmount)
        // $(".fa-shopping-basket").removeClass('item-added-transition');
    } else{
           $(".fa-shopping-basket").removeClass('item-added-transition');
    }

});


// Nav bar



// Hiding the photo upload function

$('#imageUploadWrapperTrigger').click(function(){
    $('#imageUploadWrapper').toggleClass('hide');
});

// Increasing product quantity

$('#increaseProductDetailQuantity').click(function(e){
    e.preventDefault();
    var quantity = parseInt($('#productDetailQty').val());
        
        // If is not undefined
            
            $('#productDetailQty').val(quantity + 1);
       
            $('#addToBasket').prop('disabled', false);
        
});

$('#decreaseProductDetailQuantity').click(function(e){
    e.preventDefault();
    var quantity = parseInt($('#productDetailQty').val());
        
        // If is not undefined
    if (quantity > 1){         
        $('#productDetailQty').val(quantity - 1);
    } else {
        quantity = 0;
         $('#productDetailQty').val(quantity);

        $('#addToBasket').prop('disabled', true);
    }
});

let digital_counter = 0
$("#deliveryTypeCheckbox").change(function() {
    digital_counter++;
    
    if (digital_counter % 2 == 0){
        console.log(digital_counter);
         $("#productDetailQty, #decreaseProductDetailQuantity, #increaseProductDetailQuantity").prop('disabled', false);
        var quantity = 1;
         $('#productDetailQty').val(quantity);
    } else {
        console.log("odd");
        $("#productDetailQty, #decreaseProductDetailQuantity, #increaseProductDetailQuantity").prop('disabled', true);
      var quantity = 1;
        $('#productDetailQty').val(quantity);
    }
   
});

$('#addToBasket').click(function(){
    $("#productDetailQty").prop('disabled', false);
   
});


// Review reveal

$('#reviewTrigger').click(function(){
    console.log("triggered");
    $("#reviewsWrapper").toggleClass('hide');
});


$(".linkingProductSelect").change(function() {
 console.log("function reached.");
 let val = $(this).val();
 let splittingValues = val.split("|");
 let imageType = splittingValues[2];
 let imageId = splittingValues[1]
 if (imageType == "inventory") {
    let imagePath = splittingValues[0];
    console.log(imagePath);
  $("#linkImageSelection").attr('src', imagePath);
  $("#linkedProductImagePreview").attr('href', imagePath);
   $("#linkImageHint").removeClass('hide');
  
  $("#linkImageSelection").addClass('product-linked-preview');
 } else {
     let imagePath = "/media/" + splittingValues[0];
     console.log(imagePath);
  $("#linkImageSelection").attr('src', imagePath);
  $("#linkImageSelection").addClass('product-linked-preview');
  $("#linkedProductImagePreview").attr('href', imagePath);


 }
 
});

// Update basket

$('.editBasketBodyTrigger').click(function(){
    console.log("triggered!!")
    $('.editBasketBody').toggleClass('hide');
});

$('.reset-modal-body').click(function(){
    console.log("triggered reset")
    $('.editBasketBody').addClass('hide');
});

$('.quantityModifier').click(function(e){
    e.preventDefault();
});



function updateBasket(editId, updateId, cancelId, editQuantity, editDelivery, editLinkedItem, editMode) {
    let editButton = document.getElementById(editId);
    let updateButton = document.getElementById(updateId);
    let cancelButton = document.getElementById(cancelId);
    let quantityEdit = document.getElementById(editQuantity);
    let deliveryEdit = document.getElementById(editDelivery);
    let editItem = document.getElementById(editLinkedItem);
    console.log(editItem)
    let editingMode = editMode;
    if (editingMode == 'update'){
        editButton.classList.add('hide')
        updateButton.classList.remove('hide')
        cancelButton.classList.remove('hide')
        quantityEdit.classList.remove('hide')
        deliveryEdit.classList.remove('hide')
        editItem.classList.remove('hide')
    } else {
        editButton.classList.remove('hide')
        updateButton.classList.add('hide')
        cancelButton.classList.add('hide')
        quantityEdit.classList.add('hide')
        deliveryEdit.classList.add('hide')
        editItem.classList.add('hide')
    }
    
}


$("#adminProductManage").change(function() {
    console.log("triggered")
    $('.allProducts').addClass('hide');
    let val = $(this).val();
    console.log(val);
    $(`.adminCategory${val}`).toggleClass(' hide');
    $(`#adminCategoryHR`).removeClass(' hide');
  
    
});
