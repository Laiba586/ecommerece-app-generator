class EcommmerceApp:
    def __init__(self):
        self.products = {
            '1': {'name': 'Laptop', 'price': 80000, 'quantity': 100},
            '2': {'name': 'Mobile', 'price': 50000, 'quantity': 200},
            '3': {'name': 'Tablet', 'price': 30000, 'quantity': 300}
        }
        self.cart = {}
        self.total = 0
    def display_menu(self):
        print("Welcome to the E-Commerce App!")
        print("Available Products:")
        for id, product in self.products.items():
            print(f"{id}: {product['name']} - Rs. {product['price']}")
    def display_products(self):
        print("Available Products:")
        for id, product in self.products.items():
            print(f"{id}: {product['name']} - Rs. {product['price']} - Quantity: {product['quantity']}")
    def add_to_cart(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            if product['quantity'] >= quantity:
                self.cart[product_id] = quantity
                self.total += product['price'] * quantity
                product['quantity'] -= quantity
                print(f"{quantity} {product['name']} added to cart.")
            else:
                print("Sorry, the product is out of stock.")
        else:
            print("Invalid product ID.")
    def view_cart(self):
        print("Cart:")
        for id, quantity in self.cart.items():
            product = self.products[id]
            print(f"{product['name']} - Rs. {product['price']} - Quantity: {quantity}")
        print(f"Total: Rs. {self.total}")
    def checkout(self):
        print("Checking out...")
        self.view_cart()
        print("Thank you for shopping with us!")
        self.cart = {}
        self.total = 0
    def run(self):
        while True:
            print("\nMenu:")
            print("1: Display Products")
            print("2: Add to Cart")
            print("3: View Cart")
            print("4: Checkout")
            print("5: Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.display_products()
            elif choice == '2':
                product_id = input("Enter the product ID: ")
                quantity = int(input("Enter the quantity: "))
                self.add_to_cart(product_id, quantity)
            elif choice == '3':
                self.view_cart()
            elif choice == '4':
                self.checkout()
            elif choice == '5':
                break
            else:
                print("Invalid choice!")
app = EcommmerceApp()
app.run()
