gross = 0

while gross <= 0:
    gross = input("Enter your gross income: ")
    try:
        gross = float(gross)

        rate = 0

        if 8000 <= gross < 15000:
            rate = 25
        elif 15000 <= gross < 25000:
            rate = 35
        elif 25000 <= gross < 50000:
            rate = 42
        elif gross >= 50000:
            rate = 48

        tax = gross * rate / 100
        if rate == 0:
            tax = 0

        net = gross - tax

        print(f"\nGross income: ${gross:,.2f}")
        print(f"Tax rate: {rate:.2f}%")
        print(f"Tax payable: ${tax:,.2f}")
        print(f"Net income: ${net:,.2f}")

    except ValueError:
        print("Invalid gross income")
        gross = 0
