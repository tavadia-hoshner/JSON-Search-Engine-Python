#Author:- Hoshner Tavadia
#Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca

from os import system
from utilities import search, getRecipe

def findNames():
    print("\nFind Recipe Names By Keywords")
    key = input("Enter Keyword Seperated By Space: ")
    stype = input("Enter Search Type(normal, simple or healthy): ")
    while(not(stype==("normal") or stype==("simple") or stype==("healthy"))):
          print("Invalid Search Type Try Again")
          stype = input("Enter Search Type(normal, simple or healthy): ")
    amt = input("Enter Number Of Recipes: ")
    while (not amt.isnumeric()):
        print("Invalid Number Try Again")
        amt = input("Enter Number Of Recipes: ")
    amt = int(amt)
    print()
    search(key,stype,amt)
    input("\nCopy The Name Of The Dish To Lookup The Recipe In Mode 2\nPress ENTER To Exit To Main Menu\n")
    system('CLS')
    main()


def findRecipe():
    print("\nFind Recipe By Name")
    key = input("Enter The Exact Name Of Your Dish: ")
    getRecipe(key)
    input("\nPress ENTER To Exit To Main Menu\n")
    system('CLS')
    main()
    
def main():
    print("Welcome To JSON Recipe Search Engine")
    print("""
MODES:
1.Recipe Finder Using Keywords
2.Recipe Lookup Using Name
3.Exit Program""")
    inp = input("\nEnter The Number To Choose Your Mode: ")
    inp = int(inp)
    if (inp==1):
        findNames()
    elif (inp==2):
        findRecipe()
    elif (inp==3):
        exit()
    else:
        print("Invalid Input, Try Again\n")
        input()
        system('CLS')
        main()

if __name__ == "__main__":
    main()
