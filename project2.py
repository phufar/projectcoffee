#variable
show_menu = 0
coffee = 0
coffe_type = 0
coffee_pay = 0

################################################################

#list
coffee_list = ["Espresso", "Cappucino", "Latte"]
type_list = ["Hot", "Cold"]
price_list = ["55", "60"]
coffee_list_2 = [1, 2, 3]
type_list_2 = [1, 2]
price_list_2 = [1, 2]

################################################################

#text variable
menu = "---Choose the menu--- \n 1.Espresso \n 2.Cappucino \n 3.Latte"
type_menu = "---Choose type of the coffe--- \n 1.Hot 55 Baht \n 2.Cold 60 Baht"

################################################################

#function
def show_menu_function():
    global show_menu
    show_menu = int(input("Please type 1 to show menu:"))
    return show_menu

def coffee_input():
    global coffee
    coffee = int(input("Select coffee:"))
    return coffee
    
def coffee_type_function():
    global coffee_type
    coffee_type = int(input("Select type:"))
    
    if coffee_type not in type_list_2:
        print("Something went wrong please try again")
    else:
        print(f"You choose {type_list[coffee_type-1]} {coffee_list[coffee-1]} {price_list[coffee_type-1]} bath")

    return coffee_type

def price_function():
    global coffee_pay
    coffee_pay = int(input("Input your money:"))
    if coffee_pay > int(price_list[coffee_type-1]):
        print(f"You recieved a change of {coffee_pay-int(price_list[coffee_type-1])} bath")
    elif coffee_pay == int(price_list[coffee_type-1]):
        print("Thank you,there no change")
    else:
        print("Not enough money please try again")
    return coffee_pay

################################################################

#main program
print("---Weclome to Peak's coffe---")
show_menu_function()
if show_menu == 1:
    print(menu)
    
    coffee_input()
    if coffee not in coffee_list_2 :
        print("Something went wrong please try again")
        
    else:
        print(type_menu)
        coffee_type_function()
        price_function()

else: 
    print("Something went wrong please try again")