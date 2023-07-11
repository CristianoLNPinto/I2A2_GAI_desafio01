var products = [
    {
        "id": 1,
        "product_name": "Organic Green Tea",
        "unit_price": 9.99,
        "product_image": "green_tea.png"
    },
    {
        "id": 2,
        "product_name": "Superfood Smoothie Mix",
        "unit_price": 14.99,
        "product_image": "smoothie_mix.png"
    },
    {
        "id": 3,
        "product_name": "Vegan Protein Powder",
        "unit_price": 19.99,
        "product_image": "protein_powder.png"
    },
    {
        "id": 4,
        "product_name": "Gluten-Free Granola Bars",
        "unit_price": 7.99,
        "product_image": "granola_bars.png"
    },
    {
        "id": 5,
        "product_name": "Organic Chia Seeds",
        "unit_price": 6.99,
        "product_image": "chia_seeds.png"
    },
    {
        "id": 6,
        "product_name": "Natural Almond Butter",
        "unit_price": 12.99,
        "product_image": "almond_butter.png"
    },
    {
        "id": 7,
        "product_name": "Detox Herbal Tea",
        "unit_price": 8.99,
        "product_image": "detox_tea.png"
    },
    {
        "id": 8,
        "product_name": "Organic Quinoa",
        "unit_price": 5.99,
        "product_image": "quinoa.png"
    },
    {
        "id": 9,
        "product_name": "Plant-Based Protein Bars",
        "unit_price": 10.99,
        "product_image": "protein_bars.png"
    },
    {
        "id": 10,
        "product_name": "Natural Coconut Oil",
        "unit_price": 11.99,
        "product_image": "coconut_oil.png"
    }
    // Add the remaining products from the JSON list here
];

var productGrid = document.getElementById('product-grid');

products.forEach(function (product) {
    var productCard = document.createElement('div');
    productCard.classList.add('col-md-4', 'mb-4');

    var productImage = document.createElement('img');
    productImage.src = product.product_image;
    productImage.alt = product.product_name;
    productImage.classList.add('img-fluid');

    var productName = document.createElement('h3');
    productName.textContent = product.product_name;

    var unitPrice = document.createElement('p');
    unitPrice.textContent = 'Unit Price: $' + product.unit_price.toFixed(2);

    var productId = document.createElement('p');
    productId.textContent = 'Product ID: ' + product.id;

    productCard.appendChild(productImage);
    productCard.appendChild(productName);
    productCard.appendChild(unitPrice);
    productCard.appendChild(productId);

    productGrid.appendChild(productCard);
});