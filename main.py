from os import system
from keyboard import is_pressed

def theMainGuy():
    system("cls")
    print("Hi, i'll tell you if a number is zero or not.")
    k = input("Press enter to continue.")
    
    while True:
        try:
            if is_pressed("enter"):
                system("cls")
                a = int(input("Enter a number: "))
                theGuyWhoChecksNumber(a)
                break
        except:
                system("cls")
                a = int(input("Enter a number: "))
                theGuyWhoChecksNumber(a)
                break
    
    


def theGuyWhoChecksNumber(n):
    
    if n == 0:
        #another clear
        system("cls")
        print("It's zero")
    elif n != 0:
        system("cls")
        print("It's not zero")

theMainGuy()