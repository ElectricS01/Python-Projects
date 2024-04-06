burgers = ['Cheeseburger ', 'Hamburger ', 'Double Cheeseburger ']
burgers_price = {'Cheeseburger ': 2, 'Hamburger ': 2, 'Double Cheeseburger ': 3.5}

drinks = ['Orange juice ', 'Coke ', 'Pepsi ']
drinks_price = {'Orange juice ': 2.5, 'Coke ': 4, 'Pepsi ': 4}

orders = []
orders2 = []
price = 0
breaker = False

add = ''

print('Made by ElectricS01 electrics01.com ')


# Do Not Redistribute without permission


def order():
    global orders, orders2, add, breaker, price
    while True:
        add = ''
        if len(orders) > 1:
            orders2 = orders[:-1]
        else:
            orders2 = orders
        striped = ''.join(map(str, orders2))
        if len(orders) > 1:
            add = f'and {orders[len(orders) - 1]} '

        if not orders:
            striped = 'Empty'
            add = ''

        opt7 = input(f'\nYour order is: {striped}{add}\nThis will cost: ${price} \n\nDo you want to: \n\nOrder more('
                     f'1) \nConfirm order(2) \nEdit order(3) ')
        if opt7 == '1':
            break

        elif opt7 == '2':
            if striped == 'Empty':
                print('\nOrder is empty ')
            else:
                print(f'\nYou got a {striped} {add} \nIt costed you ${price} ')
                with open('orders.txt', 'a') as f:
                    joined = ''.join(orders)
                    pvar = f'Order by {name} for: {joined}at a cost of ${price} \n'
                    f.write(pvar)
                exit()

        elif opt7 == '3':
            if striped == 'Empty':
                print('\nOrder is empty ')
            else:
                if len(orders) > 0:
                    breaker = False
                    while not breaker:
                        print()
                        for index0, ii in enumerate(orders):
                            if index0 < len(orders) - 1:
                                print(ii.strip(' ') + '(' + str(index0 + 1) + ') ')
                            else:
                                opt8 = input(ii.strip(' ') + '(' + str(index0 + 1) + ') ')
                                if opt8.isnumeric():
                                    opt8 = int(opt8)
                                    if 0 < opt8 < len(orders) + 1:
                                        while not breaker:
                                            opt9 = input(f'\nRemove(1) \n\nBack(2) ')
                                            if opt9.isnumeric():
                                                opt9 = int(opt9)
                                                if opt9 == 1:
                                                    if orders[opt8-1] in burgers:
                                                        price -= burgers_price[orders[opt8 - 1]]
                                                    else:
                                                        price -= drinks_price[orders[opt8 - 1]]
                                                    orders.pop(opt8 - 1)
                                                    breaker = True
                                                    break

                                                elif opt9 == 2:
                                                    breaker = True
                                                    break


while True:
    name = input('\nEnter your name: ')
    while name:
        print('\nWelcome to Donald\'s Burgers ')
        while True:
            breaker = False
            opt = input('\nWould you like to Order(1) or Leave(2) ')
            if opt == 'Admin':
                while not breaker:
                    opt1 = input('\nAdmin Password: ')
                    if opt1 == 'Password':
                        while True:
                            breaker = False
                            opt2 = input('\nAdd Burger(1) \nAdd Drink(2) \nRemove Item(3) \n\nExit Admin Mode(4) ')
                            if opt2 == '1':
                                while not breaker:
                                    item0 = input('Add Burger: ')
                                    if item0:
                                        item0 = item0.lower()
                                        item0 = item0.capitalize()
                                        ite0m = item0.strip(' ')
                                        burgers.append(item0 + ' ')
                                        while True:
                                            opt5 = input('Price: ')
                                            if opt5.isnumeric():
                                                opt5 = int(opt5)
                                                burgers_price[item0 + ' '] = opt5
                                                breaker = True
                                                break

                            elif opt2 == '2':
                                while not breaker:
                                    item0 = input('Add Drink: ')
                                    if item0:
                                        item0 = item0.lower()
                                        item0 = item0.capitalize()
                                        ite0m = item0.strip(' ')
                                        drinks.append(item0 + ' ')
                                        while True:
                                            opt5 = input('Price: ')
                                            if opt5.isnumeric():
                                                opt5 = int(opt5)
                                                drinks_price[item0 + ' '] = opt5
                                                breaker = True
                                                break

                            elif opt2 == '3':
                                while True:
                                    opt3 = input('\nRemove Burger(1) or Drink(2) Go back(3) ')
                                    if opt3 == '1':
                                        print()
                                        for index, i in enumerate(burgers):
                                            print(i + '(' + str(index+1) + ') ')
                                        opt4 = input(f'\nBack({len(burgers)+1}) ')
                                        if opt4.isnumeric():
                                            opt4 = int(opt4)
                                            if opt4 == len(burgers)+1:
                                                break
                                            else:
                                                print(f'Removed item {burgers[opt4-1]} ')
                                                burgers.pop(opt4-1)

                                    elif opt3 == '2':
                                        print()
                                        for index, i in enumerate(drinks):
                                            print(i + '(' + str(index+1) + ') ')
                                        opt4 = input(f'\nBack({len(drinks)+1}) ')
                                        if opt4.isnumeric():
                                            opt4 = int(opt4)
                                            if opt4 == len(drinks)+1:
                                                break
                                            else:
                                                print(f'Removed item {drinks[opt4-1]} ')
                                                drinks.pop(opt4-1)

                                    elif opt3 == '3':
                                        break

                            elif opt2 == '4':
                                breaker = True
                                break

                    else:
                        print('Incorrect Password ')
            elif opt == '1':
                while True:
                    opt0 = input('\nOrder Burger(1) or Drinks(2) ')
                    if opt0 == '1':
                        while True:
                            for index, i in enumerate(burgers):
                                print(i + '(' + str(index+1) + ') ')
                            opt6 = input(f'\nBack({len(burgers)+1}) ')
                            if opt6.isnumeric():
                                opt6 = int(opt6)
                                if opt6 == len(burgers) + 1:
                                    break
                                else:
                                    print(f'\nYou ordered a {burgers[opt6-1]} ')
                                    orders.append(burgers[opt6-1])
                                    price += burgers_price[burgers[opt6-1]]
                                    order()
                                    break

                    elif opt0 == '2':
                        while True:
                            for index, i in enumerate(drinks):
                                print(i + '(' + str(index + 1) + ') ')
                            opt6 = input(f'\nBack({len(drinks) + 1}) ')
                            if opt6.isnumeric():
                                opt6 = int(opt6)
                                if opt6 == len(drinks) + 1:
                                    break
                                else:
                                    print(f'\nYou ordered a {drinks[opt6 - 1]} ')
                                    orders.append(drinks[opt6 - 1])
                                    price += drinks_price[drinks[opt6 - 1]]
                                    order()
                                    break

            elif opt == '2':
                print('\nYou left ')
                break

        while True:
            repeat = input('\ndo you want to play again? (y/n) ')
            if repeat == 'n':
                exit()
            elif repeat == 'y':
                break
