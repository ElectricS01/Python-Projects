# Main loop so if you input an invalid resault it will ask you to input again
while True:
    # Input to  see if the light is on
    light = input("Is the light on? ")
    if light.lower() == "yes":
        # If the light is on it will exit
        print("Good, all is OK ")
        break
    elif light.lower() == "no":
        # If the light is off it will ask you if the switch is on
        electricity = input("Is the electricity turned on at the switch? ")
        if electricity.lower() == "yes":
            # If the electricity is on it will exit
            print("Turn on the electricity at the switch. ")
            break
        elif electricity.lower() == "no":
            # If the electricity is off it will ask if the light has blown
            globe = input("Has the light globe blown? ")
            if globe.lower() == "yes":
                # If the globe has blown it will exit
                print("Replace the light globe. ")
                break
            elif globe.lower() == "no":
                # If the globe has not blown it will ask if the fuse has blown
                fuse = input("Has the fuse blown? ")
                if fuse.lower() == "yes":
                    # If the fuse has blown it will exit
                    print("Replace the fuse. ")
                    break
                elif fuse.lower() == "no":
                    # If the fuse has not blown it will also exit
                    print("Call an electrician. ")
                    break
# Print at the end of the program
print("Thank you for using Trouble Shooter ")
