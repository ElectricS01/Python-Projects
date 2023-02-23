from random import randint

win = 'You won!!'
lose = 'You lost,'
lh = ('l', 'h')


def roll_dice():

    lowest = ''
    roll = 5
    player_numbers = 0
    enemy_numbers = 0

    while lowest not in lh:
        lowest = input('\nDo you want to play for lowest score or highest score?(l/h) ')
        if lowest not in lh:
            print('Invalid ')

    while roll:
        number = []
        enemy_number = []
        amount = input('\nHow many die do you want to roll? ')
        if amount.isnumeric():
            amount = int(amount)
            amount2 = amount
            amount0 = amount
            if 20 >= amount > 0:
                while True:
                    sides = input('\nHow many sides do you want your dice? ')
                    if sides.isnumeric():
                        sides = int(sides)
                        if 100 >= sides > 1:
                            while amount > 0:
                                number.append(randint(1, int(sides)))
                                amount -= 1

                            var = str(number).strip('[]')
                            print(f'Your numbers are {var}. ')

                            number = sum(number)*10
                            number = number / amount2
                            number = number / sides
                            player_numbers = number + player_numbers
                            player_numbers = round(player_numbers, 2)
                            print(f'Your total score is {player_numbers} \n')

                            while amount0 > 0:
                                enemy_number.append(randint(1, int(sides)))
                                amount0 -= 1

                            var = str(enemy_number).strip('[]')
                            print(f'The enemies numbers are {var}. ')

                            enemy_number = sum(enemy_number) * 10
                            enemy_number = enemy_number / amount2
                            enemy_number = enemy_number / sides
                            enemy_numbers = enemy_number + enemy_numbers
                            enemy_numbers = round(enemy_numbers, 2)
                            print(f'The enemies total score is {enemy_numbers} \n')

                            roll -= 1

                            break

                        else:
                            print('Invalid, too few or too many sides. ')

                    else:
                        print('Invalid ')
            else:
                print('Invalid, too few or too many die. ')

        else:
            print('Invalid ')

    else:
        if player_numbers > enemy_numbers:
            if lowest == 'l':
                printer = lose
            else:
                printer = win
        else:
            if lowest == 'h':
                printer = lose
            else:
                printer = win

        print(f'{printer} enemy had {enemy_numbers} and you had {player_numbers}. \n')

        input('Play again? ')


print('Made by ElectricS01 electrics01.com ')
# Do Not Redistribute without permission

print('\nHello, welcome to dice game. \nIn this game you roll dice and get points to win. \nThe amount of die rolled '
      'and the sides of the die divides the total score. \nAt the end of 5 rounds who ever has the lowest or highest '
      'score wins. ')

while True:
    roll_dice()
