from random import randint

rep = "y"

a = ["Ouch!", "Oops!", "Wow!", "Happy birthday!"]
b = ["Run", "Danc", "Slid", "crawl"]
c = ["Fish Tank", "Classroom", "Bike", "Tree"]
d = ["funny", "crazy", "loud", "quiet", "painful"]

print("Made by ElectricS01 electrics01.com ")

# Do Not Redistribute


while rep == "y" or "yes":
    print("Type \"Random\" or \"R\"To select a random message.")

    exc = str.casefold(input("Give me an exclamation (Ouch! Oops! Wow!) "))
    if ("random" or "r") in exc:
        exc = a[randint(0, 3)]
    ver = str.casefold(input("Give me a verb (Run, Dance, Slide) "))
    if ("random" or "r") in ver:
        ver = b[randint(0, 3)]
    nou = str.casefold(input("Give me a noun (Fish Tank, Classroom, Bike) "))
    if ("random" or "r") in nou:
        nou = c[randint(0, 3)]
    adj = str.casefold(input("Give me an adjective (Funny, Crazy, Loud) "))
    if ("random" or "r") in adj:
        adj = d[randint(0, 4)]
    print(f"I was {ver}ing down the road when I hit a {nou}, I screamed {exc} I thought it was very {adj}.")
    print()
    rep = str.casefold(input("Again?(y/n)"))
    print()
