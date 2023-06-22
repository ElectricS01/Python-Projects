from task4 import input04
from task7 import input07
from numericTask5 import pinput05

while True:
    task = input("Task number to run (4, 5, 7): ")
    print()
    if task == "4":
        input04()
    elif task == "7":
        input07()
    elif task == "5":
        pinput05()
    print()
