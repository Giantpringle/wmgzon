window.onload = function() {
    fetchProducts();
};

function fetchProducts(searchTerm = '') {
    fetch(`/products?search=${searchTerm}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const productGrid = document.getElementById('product-grid');
        productGrid.innerHTML = '';
        data.forEach(product => {
            const productCard = `
                <div class="product-card">
                    <img src="${product.image}" alt="${product.name}" />
                    <h3>${product.name}</h3>
                    <p>${product.description}</p>
                    <p>$${product.price}</p>
                    <a href="#" class="explore-button">Explore Product</a>
                </div>
            `;
            productGrid.innerHTML += productCard;
        });
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
}

function searchProducts() {
    const searchBox = document.getElementById('searchBox'); // Ensure you have an input element with id 'searchBox' in your HTML
    const searchTerm = searchBox.value.toLowerCase();
    fetchProducts(searchTerm);
}
