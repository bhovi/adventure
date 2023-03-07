name=input("type your name!")
print("welcome", name,"to this adventure!")
answer=input("you are on a dirt road, it has come to an end and you can go left or right. which way would you like to go??").lower()
if answer=="left":
    answer=input("you come to a river,you can walk around it or swim across? type walk to walk around and swim if you want to swimcross:")
    if answer=="swim":
        print("you swam across the river and were eaten by an aligator")
    elif answer=="walk":
        print("you walked miles, ran out of water and lost the game.")
    else:
        print("not a valid option. You lose")
elif answer=="right":
    answer=input("You came across a bridge, it looks wobbly, do you want to cross it or head back (cross/back) ?")
    if answer=="back":
        print("You go back and lose")
    elif answer=="cross":
        print=input("you cross the bridge and met a stranger. do yoy want to talk to him(yes/no)")
        if answer=="yes":
            print("you talk to the stranger and they gift you the treasure. you won!!!")
        elif answer=="no":
            print("you ignore the stranger and they get offended and you lose")
        else:
            print("invalid option you lose")
    else:
        print("invalid option you lose")
else:
    print("invalid option you lose!!!!")
print("Thank you for trying ",name)