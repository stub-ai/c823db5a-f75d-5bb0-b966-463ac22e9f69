import csv

class POSMachine:
    def __init__(self):
        self.price_list = {}
        self.current_transaction = {}

    def start(self):
        while True:
            try:
                self.printWelcomeMessage()
                self.printAllOptions()
                user_input = input("Enter your command: ")
                if user_input == "1":
                    self.setPriceList()
                elif user_input == "2":
                    self.printPriceList()
                elif user_input == "3":
                    self.makeNewTransaction()
                elif user_input == "4":
                    break
                else:
                    print("Invalid command. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def printWelcomeMessage(self):
        print("Welcome to the POS Machine!")

    def printAllOptions(self):
        print("1. Set price list")
        print("2. Show price list")
        print("3. New transaction")
        print("4. Close machine")

    def setPriceList(self):
        file_path = input("Enter the path of the price list file (.csv or .txt): ")
        if not file_path.endswith(('.csv', '.txt')):
            print("Invalid file type. Please try again with a .csv or .txt file.")
            return
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            self.price_list = {rows[0]:float(rows[1]) for rows in reader}
        print("Price list updated successfully.")

    def printPriceList(self):
        for product, price in self.price_list.items():
            print(f"Product ID: {product}, Price: {price}")

    def makeNewTransaction(self):
        self.current_transaction = {}
        while True:
            product_id = input("Enter product ID (or 'done' to finish): ")
            if product_id.lower() == 'done':
                break
            quantity = int(input("Enter quantity: "))
            self.addProductToTransaction(product_id, quantity)
        self.createSalesInvoice()

    def addProductToTransaction(self, product_id, quantity):
        if product_id not in self.price_list:
            print("Invalid product ID. Please try again.")
            return
        if product_id in self.current_transaction:
            self.current_transaction[product_id] += quantity
        else:
            self.current_transaction[product_id] = quantity

    def createSalesInvoice(self):
        total_amount = 0
        invoice = "Sales Invoice:\n"
        for product_id, quantity in self.current_transaction.items():
            price = self.price_list[product_id]
            amount = price * quantity
            total_amount += amount
            invoice += f"Product ID: {product_id}, Price: {price}, Quantity: {quantity}, Amount: {amount}\n"
        invoice += f"Total Amount: {total_amount}"
        print(invoice)
        with open('sales_invoice.txt', 'w') as file:
            file.write(invoice)
        print("Sales invoice saved to 'sales_invoice.txt'.")

if __name__ == "__main__":
    pos_machine = POSMachine()
    pos_machine.start()