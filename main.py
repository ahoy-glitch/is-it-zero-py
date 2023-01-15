from os import system
from keyboard import is_pressed

def theMainGuy():
    #clear
    system("cls")
    print("Hi, i'll tell you if a number is zero or not.")
    print("Press enter to continue.")
    
    while True:
        try:
            if is_pressed("enter"):
                system("cls")
                a = int(input("Enter a number: "))
                theGuyWhoChecksNumber(a)
                #breaking the loop
                break
        except: 
                system("cls")
                a = int(input("Enter a number: "))
                theGuyWhoChecksNumber(a)
                #same
                break
    
    


def theGuyWhoChecksNumber(n):
    if n == 0:
        #another clear
        system("cls")
        print("It's zero")
    elif n != 0:
        #another clear
        system("cls")
        print("It's not zero")
#calling the main guy function
theMainGuy()