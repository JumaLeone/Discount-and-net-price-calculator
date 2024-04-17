class ITEMINFO:
    def __init__(self):
        self.ICode = 0
        self.Item = ""
        self.Price = 0
        self.Qty = 0
        self.Discount = 0
        self.Netprice = 0

    def FindDisc(self):
        if self.Qty <= 10:
            self.Discount = 0
        elif 11 <= self.Qty <= 20:
            self.Discount = 0.15 * self.Price * self.Qty
        else:
            self.Discount = 0.20 * self.Price * self.Qty

        self.Netprice = self.Price * self.Qty - self.Discount

    def Buy(self):
        self.ICode = int(input("Enter Item Code: "))
        self.Item = input("Enter Item Name: ")
        self.Price = float(input("Enter Price of each item: "))
        self.Qty = int(input("Enter Quantity in stock: "))
        self.FindDisc()

    def ShowAll(self):
        print("Item Code:", self.ICode)
        print("Item Name:", self.Item)
        print("Price of each item:", self.Price)
        print("Quantity in stock:", self.Qty)
        print("Discount:", self.Discount)
        print("Net Price:", self.Netprice)


# Instantiate an object of the class ITEMINFO
item = ITEMINFO()

# Call Buy method to input values and calculate discount and net price
item.Buy()

# Call ShowAll method to display all the data members
item.ShowAll()

