def input07():
    bal = input("Enter opening balance: ")
    interest = input("Enter interest rate: ")
    bal = float(bal)
    interest = float(interest)
    print(f"Old balance: ${bal:,.2f}")
    print(f"Interest rate: {interest}%")
    print(f"Interest: ${bal * interest / 100:,.2f}")
    print(f"New balance: ${bal + bal * interest / 100:,.2f}")
