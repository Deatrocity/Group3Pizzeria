var cartItemQuantity = 0;

// handles total cart count to display on nav link
function cartCounter() {
    cartItemQuantity += 1;
    var cartCount = document.getElementById("cartCount").innerHTML = " (" + cartItemQuantity + ")";
    sessionStorage.setItem(cartCount);
};

// keeps track of total number of items in cart
function cartTotal() {
    var total = 0;
    for (let i = 0; i < cartItems.length; i++) {
        total += cartItems[i].price;
    }
    document.getElementById('cart-total').innerHTML = "Total: $" + total.toFixed(2);
}

cartItems = JSON.parse(sessionStorage.getItem('cartItem')) || [];

// adds items to cart when button is pressed
function addToCart(name, price) {
    cartItems.push({name: name, price: price });
    updateCart();
    cartCounter();
}

// updates the current session cart
function updateCart() {
    sessionStorage.setItem('cartItem', JSON.stringify(cartItems));
}

var addToCartButtons = document.getElementById('.add-to-cart');
addToCartButtons.forEach(function(button) {
    button.addEventListener('click', function(item) {
        addToCart(item.name, item.price);
    });
});

// displays the cart information
function displayCart() {
    var cartItemStrings = cartItems.map(function(item) {
        return item.name + ': $' + item.price;
    });

    if (cartItemStrings.length > 0) 
    {
        document.getElementById("cart-info").innerHTML = cartItemStrings.join("\n"); 
        document.getElementById('cart-quantity').innerHTML = cartItems.length + " Items";
    }
    else 
    {
        document.getElementById("cart-info").innerHTML = "Your cart is empty!";
    }
    
    cartTotal();
};

// clears the current cart
function clearCart() {
    cartItems = [];
    updateCart();
    displayCart();
}