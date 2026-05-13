# Program 9 — Comprehension Challenge

# Given this data:
products = [
    {"name": "Laptop", "price": 45000, "in_stock": True},
    {"name": "Mouse",  "price": 500,   "in_stock": False},
    {"name": "Keyboard","price": 1200, "in_stock": True},
    {"name": "Monitor","price": 12000, "in_stock": True},
    {"name": "Webcam", "price": 2000,  "in_stock": False},
]

# Using comprehensions only:
	
	
# 1. List of all product names
names = [product["name"] for product in products]
print(names)


#2. List of in-stock product names only
stock_names = [product["name"] for product in products if product["in_stock"] == True]
print(stock_names)


#3. Dict of {name: price} for in-stock only
stock_names_price = {product["name"] : product["price"] for product in products if product["in_stock"] == True}

print(stock_names_price)


#4. List of products with price above 1000
product_above_1000 = [product for product in products if product["price"] > 1000]

for product in product_above_1000 :
	print(product)


#5. Total value of all in-stock products
stock_products_price = [product["price"] for product in products if product["in_stock"] == True]

print(f"Total value: Rs.{sum(stock_products_price)}")
