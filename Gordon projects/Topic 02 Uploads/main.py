from task4 import concat4
from task8 import var08
from task11 import var11
from task14 import var14

while True:
    task = input("Task number to run (4, 8, 11, 14): ")
    print()
    if task == "4":
        concat4()
    elif task == "8":
        var08()
    elif task == "11":
        var11()
    elif task == "14":
        var14()
    print()
