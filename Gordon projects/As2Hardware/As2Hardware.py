# Made by ElectricS01
# Wed 21 Jun 2023
# As2Hardware.py

# Define a function to write to As2Hardware.txt
def writeFile(data):
    print(data)
    file = open("output.txt", "a")
    file.write(f"{data}\n")
    file.close()


# Get customer name
name = input("Enter your name: ")

# Define 2 variables
item = 1
total = 0

# Loop to get price of all items
while True:
    # Try catch to ensure price is a number
    try:
        price = float(input(f"Price of item number {item} (Type 0 to end): "))
        if price != 0:
            # Add price to total and increment item number by 1
            total += price
            item += 1
        else:
            # Break out of loop when price is 0
            break
    except ValueError:
        # Print error message if price is invalid
        print("Invalid price")

# Print total
print(f"Total: ${total:0.2f}\n")

# List of payment methods that is easily editable for latter use
methods = ["C: Credit", "M: Money"]

# List the payment methods to the user
for method in methods:
    print(method)

# Define a variable to store the payment method
payment = ""

# Loop to ensure payment method is valid
while payment != "c" and payment != "m":
    # Get payment method from user and convert to lowercase to make it easier to compare later on
    payment = input("Enter your payment method: ").lower()

    # Check if the payment method is Money
    if payment == "m":
        # Print and define a variable before the amount tendered is checked
        print("BRUNNINGS WAREHOUSE - Cash Transaction\n")
        tendered = ""
        while tendered == "":
            # Get amount tendered from user and check if it is a number and if it is greater than the total of the items
            tendered = input(f"Enter amount tendered: ")
            if not tendered.isnumeric() or int(tendered) < total:
                print("Invalid amount")
                tendered = ""

        # Print and end the program by parsing a message to the writeFile function
        dif = int(tendered) - total
        writeFile(f"Thank you for your payment...{name}\n\nTotal: ${total:0.2f}\n"
                  f"Amount tendered: {int(tendered):0.2f}\nChange: ${dif:0.2f}")

    # Check if the payment method is Credit and the total is less than $20.00
    elif total < 20 and payment == "c":
        # Print and define a variable before the amount tendered is checked
        print(f"BRUNNINGS WAREHOUSE - Cash Transaction\nTotal: ${total:0.2f} is less than $20.00\nPayment "
              f"must be by cash\n\n")
        tendered = ""
        while tendered == "":
            # Get amount tendered from user and check if it is a number and if it is greater than the total of the items
            tendered = input(
                f"Enter amount tendered: ")
            if not tendered.isnumeric() or int(tendered) < total:
                print("Invalid amount")
                tendered = ""

        # Print and end the program by parsing a message to the writeFile function
        dif = int(tendered) - total
        writeFile(
            f"Thank you for your payment...{name}\n\nTotal: ${total:0.2f}\nAmount tendered: ${int(tendered):0.2f}\n"
            f"Change: ${dif:0.2f}")

    # Check if the payment method is Credit and the total is greater than $20.00
    elif payment == "c":
        # Print and end the program by parsing a message to the writeFile function
        writeFile(f"BRUNNINGS WAREHOUSE - Credit Transaction\nThank you for your payment...{name}\n\n"
                  f"Total: ${total:0.2f}\nCREDIT CARD PAYMENT ACCEPTED")

    # If the payment method is invalid, print an error message
    else:
        print("Invalid payment method")
