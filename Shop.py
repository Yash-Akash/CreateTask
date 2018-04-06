import tkinter

#Main
potionCount = 0

def buyItems (resources):
    if resources != 0:
        itemChoice = str(input("What item would you like to buy?"))
        if itemChoice == "Potion":
            buyConfirmation = input("Ok that will cost 20 resources to buy. Are you sure?")
            if buyConfirmation == "yes" ,"Yes":
                print("Okay you have one potion.")
                potionCount += 1
            else:
                print("Okay exiting shop...")
        elif itemChoice == "Heal":




