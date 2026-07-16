shopping_cart = {
    "Milk": 30,
    "Bread": 10,
    "Chocolate": 25,
    "Chips": 40,
    "Apple": 20,
    "Coffee": 120,
    "Yogurt": 45
}

total_price = 0
expensive_products = []
cart_with_vat = {}

for key, value in shopping_cart.items():
    total_price += value
    if value >= 30:
        expensive_products.append(key)

    new_price = value * 1.20
    cart_with_vat[key] = new_price
print(f"Total price: {total_price}")
print(f"Expensive products: {expensive_products}")
print(f"Cart: {cart_with_vat}")

