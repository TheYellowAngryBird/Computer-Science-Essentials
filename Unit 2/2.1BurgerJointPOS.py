#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
name = -1
menu = -1
orderComplete = False
totalCost = 0
tax = 0.06
burgerChoice = -1
sideChoice = -1
drinkChoice = -1

#WELCOME THE USER TO THE POINT OF SALE(POS)
print()
print()
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print()

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()


#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        print("Burgers")
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger; $5.50")
        print("2: Cheeseburger; $6.00")
        print("3: Western burger, (Cheese, onion, western sauce); $6.75")
        print("4: Peanut Butter Bacon Burger, (Peanut Butter, Bacon,); $7.50")
        burgerChoice = input("What would you like (input a number 1-4): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost + 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
        
        #BURGER 4: ADD ONE HERE
            #ADD A NEW BURGER OPTION AND UPDATE ALL CODE ABOVE TO MAKE IT WORK
        elif burgerChoice =="4":
            totalCost = totalCost + 7.50
            print("You added Peanut Butter Bacon Burger to your order")
            print("Your total cost so far: $", totalCost)
            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("Please select a valid option")
        
    elif menu == "Sides":
        print("Sides")
        #Add your Code/Comments Here for sides
        print("We offer the following sides:")
        print("1: Fries; $3.00")
        print("2: Onion Rings; $3.50")
        print("3: Mozzerella Sticks; $4.00")
        sideChoice = input("What would you like (input a number 1-3): ")
        #Add at least three sides
        if sideChoice == "1":
            totalCost = totalCost + 3.00
            print("You added Fries to your order")
            print("Your total cost so far: $", totalCost)
        elif sideChoice == "2":
            totalCost = totalCost + 3.50
            print("You added Onion Rings to your order")
            print("Your total cost so far: $", totalCost)
        elif sideChoice == "3":
            totalCost = totalCost + 4.00
            print("You added Mozzerella Sticks to your order")
            print("Your total cost so far: $", totalCost)
        else:
            print("Please select a valid option")
    elif menu == "Drinks":
        print("Drinks")
        #Add Your code/Comments here for Drinks
        print("We offer the following drinks:")
        print("1: Water; $1.50")
        print("2: Lemonade; $2.50")
        print("3: Coca-Cola; $3.50")
        drinkChoice = input("What would you like (input a number 1-3): ")
        #Add at least three drinks
        if drinkChoice == "1":
            totalCost = totalCost + 1.50
            print("You added Water to your order")
            print("Your total cost so far: $", totalCost)
        elif drinkChoice == "2":
            totalCost = totalCost + 2.50
            print("You added Lemonade to your order")
            print("Your total cost so far: $", totalCost)
        elif drinkChoice == "3":
            totalCost = totalCost + 3.50
            print("You added Coca-Cola to your order")
            print("Your total cost so far: $", totalCost)
        else:
            print("Please select a valid option")
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print()

        #GIVE THEM THEIR TOTALS
        print("Order Finished")
        print(name)
        print("You have ordered")
        print("Burger Option:",burgerChoice)
        print("Side Option:",sideChoice)
        print("Drink Option:",drinkChoice)
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * tax
        print("Total Tax: $", totalTax)
        Total = totalCost + totalTax
        print("Grand Total: $", Total)
        #Finish this section to give you a grand total as well as print your complete order
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us!")
