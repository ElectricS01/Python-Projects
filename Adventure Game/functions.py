location = 'start'

breaker = True
breaker0 = True
breaker1 = True
breaker2 = True

direction = ''
light = ''
var = ''
start = ''
gotonext = ''
campfires = ''
rivers = 'incomplete'
wood = 'incomplete'

wounded = False
cg = False

equipment = ['Food', 'Water']
eqa = ['gun', 'knife', 'lighter', 'extra food']
lva = ['river', 'mountain', 'woods']
aca = ['go back', 'keep going']
bea = ['run', 'attack']
yn = ['y', 'n']
gn = ['gun', 'knife']
mf = ['Meat', 'Food']

print("Made by ElectricS01 electrics01.com ")


# Do Not Redistribute without permission


def directions():
    global location
    global gotonext
    global direction

    while True:

        direction = input('Where do you want to go now?(River, Mountain or Woods) ').lower()
        print()

        if direction in lva:
            location = direction.title()
            direction = ''
            break

        else:
            print('Option invalid ')

    print(f'You went to the {location}. ')
    move()


def move():
    if location == 'Mountain':
        if cg:
            mountain()
        else:
            print("You didn't have climbing gear, you slipped on the rocks and Died!! \n\n")

    if location == 'River':
        if rivers == 'complete':
            river2()
        else:
            river()

    if location == 'Woods':
        if wood == 'complete':
            woods2()
        else:
            woods()


def river():
    print('You see a bear in the water. ')
    global gotonext
    while gotonext == '':
        action = input(f'What do you do?(Go back or Keep going) ').lower()
        print()
        if action in aca:
            if action == 'go back':
                print('You went back. ')
                directions()

            if action == 'keep going':
                print('The bear sees you. ')

                global breaker
                while breaker:
                    bear = input('What do you do?(Run or Attack) ').lower()
                    print()
                    if bear in bea:
                        if bear == 'run':
                            print('The bear chased you down and killed you! ')
                            break

                        if bear == 'attack':
                            attack = input(f'Use {equipment[0]}, {equipment[1]}, {equipment[2]}. ').lower()

                            while attack.title() in equipment:
                                if attack.title() == equipment[0]:
                                    print('The bear killed you! ')
                                    breaker = False
                                    gotonext = 'end'
                                    break

                                if attack.title() == equipment[1]:
                                    print('The bear killed you! ')
                                    breaker = False
                                    gotonext = 'end'
                                    break

                                if attack.title() == equipment[2]:
                                    global rivers
                                    if equipment[2] == 'Gun':
                                        print('You killed the bear ')
                                        breaker = False
                                        gotonext = 'end'
                                        rivers = 'complete'
                                        campfire()
                                        break

                                    if equipment[2] == 'Knife':
                                        print('You killed the bear but you are wounded ')
                                        breaker = False
                                        gotonext = 'end'
                                        global wounded
                                        wounded = True
                                        rivers = 'complete'
                                        campfire()
                                        break

                                    if equipment[2] == 'Lighter':
                                        print('The bear killed you! ')
                                        breaker = False
                                        gotonext = 'end'
                                        break

                                    if equipment[2] == 'Extra Food':
                                        print('The bear killed you! ')
                                        breaker = False
                                        gotonext = 'end'
                                        break

        else:
            print('Option invalid ')


def river2():
    while True:
        get_water = input('Do you want to get water?(y/n) ').lower()
        if get_water == 'y':
            water = equipment.count('Water')
            if water <= 4:
                equipment.append('Water')
                print(f'\nYou have {water} water. \n')
                directions()
                break
            else:
                print('\nYou have to much water. \n')
                directions()
                break
        else:
            print()
            directions()
            break


def campfire():
    print('\nIt\'s getting dark. ')
    while campfires == '':
        global light
        light = input('Do you want to make a campfire(y/n) ').lower()
        if light in yn:
            if light == 'y':
                print('\nYou lit the campfire')
                if equipment[0] == 'Food':
                    equipment.remove('Food')
                if equipment[0] == 'Water':
                    equipment.remove('Water')
                    global wounded
                    if wounded:
                        wounded = False
                        print('Your wounds have healed. ')
                    print('You were hungry, you cooked your food. ')
                    print('You were thirsty, you drank your water. \n')
                    directions()
                    break

            if light == 'n':
                print('\nIt\'s very cold\n ')
                directions()
                break

        else:
            print('Option invalid ')


def woods():
    print('You hear wolves in the distance. \n')
    global breaker2
    while breaker2:
        chase = input('Do you chase after them?(y/n) ').lower()
        if chase in yn:

            if chase == 'y':
                print('You step on a stick, the wolves hear you. \n')
                global breaker1
                while breaker1:

                    hide = input('Do you hide?(y/n) ').lower()
                    if hide in yn:

                        if hide == 'y':
                            print("The wolf's didn't see you. ")
                            breaker2 = False
                            cabin()
                            break

                        if hide == 'n':
                            global var
                            global breaker0
                            while breaker0:
                                if len(equipment) == 1:
                                    var = f'{equipment[0]} '
                                if len(equipment) == 2:
                                    var = f'{equipment[0]} {equipment[1]} '
                                if len(equipment) == 3:
                                    var = f'{equipment[0]} {equipment[1]} {equipment[2]} '
                                if len(equipment) == 4:
                                    var = f'{equipment[0]} {equipment[1]} {equipment[2]} {equipment[3]} '
                                if len(equipment) == 5:
                                    var = f'{equipment[0]} {equipment[1]} {equipment[2]} {equipment[3]} {equipment[4]} '

                                attack = input(f'Use {var} ').lower()

                                while attack.title() in equipment:
                                    if attack in gn:
                                        if 'gun' in attack:
                                            global wounded
                                            if wounded:
                                                print('You ran out of ammo, the wolves killed you! ')
                                                breaker0 = False
                                                breaker1 = False
                                                breaker2 = False
                                                break
                                            else:
                                                wounded = True
                                                print('You ran out of amo and the wolves injured you. ')
                                                food()
                                                breaker0 = False
                                                breaker1 = False
                                                breaker2 = False
                                                break

                                        if 'knife' in attack:
                                            print('You killed all the wolves. ')
                                            food()
                                            breaker0 = False
                                            breaker1 = False
                                            breaker2 = False
                                            break

                                    else:
                                        print('The wolves killed you! ')
                                        breaker0 = False
                                        breaker1 = False
                                        breaker2 = False
                                        break

                    else:
                        print('Option invalid ')

            if chase == 'n':
                cabin()
                break

        else:
            print('Option invalid ')


def food():
    print('You also got meat from the wolves, maybe you can cook it. \n')
    equipment.append('Meat')
    cabin()


def cabin():
    while True:
        enter = input('You find a cabin, do you check it out?(y/n) ').lower()

        if enter in yn:
            if enter == 'y':
                if enter in mf:

                    global wounded

                    if 'Meat' in equipment:
                        print('There is a camp fire lit, you cook your meat and eat it ')
                        equipment.remove('Meat')
                        if wounded:
                            wounded = False
                            cabin2()
                            break

                    else:
                        if 'Food' in equipment:
                            print('There is a camp fire lit, you cook your food and eat it ')
                            equipment.remove('Food')
                            if wounded:
                                wounded = False
                                cabin2()
                                break

                        else:
                            print('Error mf297 ')

                else:
                    print('There is a lit campfire but you have no food ')
                    cabin2()
                    break

            if enter == 'n':
                print('You keep walking for a while until you get to cold, you lay down on the ground and die. \n')
                break


def cabin2():
    global wood
    if 'gun' in equipment:
        print('In the cabin you find climbing gear and extra bullets. \n')
        wood = 'complete'
        directions()

    else:
        print('In the cabin you find climbing gear. ')
        global cg
        cg = True
        wood = 'complete'
        directions()


def mountain():
    print('You use your climbing gear to climb up the mountain. \n')
    print('Eventually you climb to a ledge where you stop to rest \n')
    print('You hear a distant roar when all of a sudden there is an avalanche. \n')
    print('You fall of the mountain and die. ')


def woods2():
    print('You go back to the cabin')
    if 'Food' in equipment:

        print('There is a camp fire lit, you cook your food and eat it ')
        equipment.remove('Food')
        global wounded
        if wounded:
            wounded = False
    directions()


def game_start():
    while True:
        name = ''
        while start == '':

            while not name:
                name = input('Name: ')
                if name:
                    print(f'\nHello! {name}, Welcome to the forest of DOOM!! ')
                    break

            bring = input('What will you bring with you?(Gun, Knife, Lighter or  Extra Food) ').lower()
            print()
            if bring in eqa:
                equipment.append(bring.title())
                print(f'Your equipment is {equipment[0]}, {equipment[1]}, {equipment[2]}.\n ')
                directions()
                break
            else:
                print('Option invalid ')

