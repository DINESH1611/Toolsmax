function addToCart(productName, price, imageSrc) {
    // Create a new item object
    const item = { name: productName, price: price, image: imageSrc, quantity: 1 };

    // Get the cart from local storage or initialize an empty array
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Check if the item is already in the cart
    const existingItem = cart.find(i => i.name === productName);
    if (existingItem) {
        existingItem.quantity++; // If so, increment its quantity
    } else {
        cart.push(item); // Otherwise, add the item to the cart
    }

    // Save the updated cart back to local storage
    localStorage.setItem('cart', JSON.stringify(cart));

    // Log the cart to check its contents
    console.log(cart);

    // Update the cart display
    displayCart();
}
// Function to display cart items
function displayCart() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Log the cart to check if it's being retrieved correctly
    console.log(cart);

    const cartItemsDiv = document.getElementById('cart-items');
    cartItemsDiv.innerHTML = ''; // Clear previous items

    // Loop through cart items and create HTML elements
    cart.forEach(item => {
        const itemDiv = document.createElement('div');
        itemDiv.innerHTML = `
            <div class="cart-item">
                <img src="${item.image}" alt="${item.name}">
                <div class="item-details">
                    <h3>${item.name}</h3>
                    <p>Price: $${item.price}</p>
                    <p>Quantity: ${item.quantity}</p>
                    <button onclick="incrementItem('${item.name}')">+</button>
                    <button onclick="decrementItem('${item.name}')">-</button>
                    <button onclick="removeItem('${item.name}')">Remove</button>
                </div>
            </div>
        `;
        cartItemsDiv.appendChild(itemDiv);
    });

    // Calculate and display total amount
    const totalAmountSpan = document.getElementById('total-amount');
    const totalAmount = cart.reduce((acc, item) => acc + item.price * item.quantity, 0);
    totalAmountSpan.textContent = `$${totalAmount.toFixed(2)}`;
}
