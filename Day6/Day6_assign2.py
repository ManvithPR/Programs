class Supermarket:
    def __init__(self):
        self.products = []

    def add_product(self, name, qty, price):
        self.products.append([name, qty, price])

    def display_bill(self):
        grand_total = 0
        max_price = 0
        expensive_product = ""

        print("\n-----------------------")
        print("Product Total")
        print("-----------------------")

        for product in self.products:
            name = product[0]
            qty = product[1]
            price = product[2]

            total = qty * price
            grand_total += total

            print(name, total)

            if price > max_price:
                max_price = price
                expensive_product = name

        print("\nGrand Total :", grand_total)

        print("\nMost Expensive Product :", expensive_product)

        print("\nProducts Above ₹1000:")
        for product in self.products:
            name = product[0]
            qty = product[1]
            price = product[2]

            if qty * price > 1000:
                print(name)


# Main Program
market = Supermarket()

for i in range(5):
    print(f"\nEnter Details for Product {i+1}")
    name = input("Product Name : ")
    qty = int(input("Qty : "))
    price = float(input("Price : "))

    market.add_product(name, qty, price)

market.display_bill()