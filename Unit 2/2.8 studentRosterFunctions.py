

#This program aims to teach you about arrays and the linear search function

#In this program, you have a list of items and need to find if a specific item is in that list


#example array
#an array is a list of items seperated by a ','
#you can add to, remove from, search through, find length of the list
students_signed_up_for_senior_trip = ["John", "Mary", "David", "Emily", "Michael", "Emma", "Daniel", "Olivia", "James", "Sophia", 
         "William", "Ava", "Alexander", "Isabella", "Joseph", "Charlotte", "Matthew", "Amelia", "Andrew", 
         "Mia", "Christopher", "Harper", "Benjamin", "Evelyn", "Nicholas"]

#The following code is called a FUNCTION. It is like a recipe and can be called unlimited times
#A function requires three things:
#1) def or define declares the start of a function
#2) name of your function. Below it is getNumStudents
#3) Parameters. these are items that are needed for the function to run
#they go in the (). The one below is empty because it does not require any parameters to run

#This function returns the length of the list
def getNumStudents():
    number_of_students_going_on_senior_trip = len(students_signed_up_for_senior_trip)
    return number_of_students_going_on_senior_trip

#This code adds a student to the list
def addStudentToList(name):
    students_signed_up_for_senior_trip.append(name)

#This function searches the list to see if a student is on the list and returns a 'yes' or 'no'
def searchList(name):
    for i in range(len(students_signed_up_for_senior_trip)):
        if students_signed_up_for_senior_trip[i] == name:
            return "yes"
    return "no"
        
#This function prints the list to the terminal for viewing
def printList():
    print(students_signed_up_for_senior_trip)

#All functions are listed above the main code of the program.
    
#MAIN CODE:
#loop infinitely until you break 
while True:

    #Welcome Message and Menu of options
    print("Student Roster Maker V1.1")
    print("What would you like to do?")
    print("1: Add student to list")
    print("2: Check if a student is on the list")
    print("3: View number of students on list")
    print("4: View students on the list")
    print("5: Exit Program")
    #store their choice and go to the appropriate option below
    choice = input("->")

    if choice == "1":
        #Add Student to List
        print("What name would you like to add to the list")
        #store their choice
        name_choice = input("->")
        try:
            #If successful, add their name to the list
            addStudentToList(name_choice)
            print("Successfully added ", name_choice, "to the list")
        except:
            #if not successful, print an error to avoid crashing
            print("Error adding name to list")
    
    elif choice == "2":
        print("What name would you like to check for on the list?")
        name = input("->")
        if searchList(name) == "yes":
            print(name, "is on the list")
        else:
            print(name, "is not on the list")
    elif choice == "3":
        number_of_students_going_on_senior_trip = len(students_signed_up_for_senior_trip)
        print("The number of students on the list is", number_of_students_going_on_senior_trip)
    elif choice == "4":
        print(students_signed_up_for_senior_trip)
    elif choice == "5":
        print("You have successfully exited the program")
        break
    else:
        print("You have entered an invalid choice, please try again")
#END OF CODE
