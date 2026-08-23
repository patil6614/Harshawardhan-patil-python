
#27-Create dictionary containing product names and quantities
products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15
}

# Add a product
products["Bottle"] = 8

# Update quantity
products["Book"] = 12

# Delete a product
products.pop("Pen")

# Search for a product
product = "Bag"

if product in products:
    print("Product found:", product, products[product])
else:
    print("Product not found")

# Display products with quantity below 10
print("Products with quantity below 10:")

for product, quantity in products.items():
    if quantity < 10:
        print(product, quantity)

