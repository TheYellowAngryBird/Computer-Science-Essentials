#Homeroom Roster Program
#This program is designed to allow a teacher to:
#1) See students in homeroom, #2) Add/Remove Students to homeroom
#3) See basic info about students

#create an object called Student
class Student:
    def __init__(self, name, grade, ID, address, age, locker_number):
        self.name = name
        self.grade = grade
        self.ID = ID
        self.address = address
        self.age = age
        self.locker_number = locker_number

list_of_homeroom_students = []

#Functions
def add_to_homeroom():
    #Create a new student object with the following properties:
    #name, grade, ID, address, age, locker_number

    #Name
    print("Creating New Student:")
    print("What is their name?")
    name = input("->")

    #Grade
    print("What is their grade?")
    grade = input("->")

    #ID
    print("What is their ID number?")
    ID_number = input("->")

    #Address
    print("What is their address?")
    address = input("->")

    #Age
    print("What is their age?")
    age = input("->")

    #Locker Number
    print("What is their locker number?")
    locker = input("->")

    #Create the student object using the variables created above
    #name, grade, ID, address, age, locker_number
    baked_potato = Student(name, grade, ID_number, address, age, locker)
    list_of_homeroom_students.append(baked_potato)
    print("Created a student with the details below:")
    print("Name:", baked_potato.name)
    print("Grade:", baked_potato.grade)
    print("ID Number:", baked_potato.ID)
    print("Address:", baked_potato.address)
    print("Age:", baked_potato.age)
    print("Locker Number:", baked_potato.locker_number)

def get_number_of_students():
    number_of_homeroom_students = len(list_of_homeroom_students)
    return number_of_homeroom_students
def search_list_for_student(search_name):
    for counter in list_of_homeroom_students:
        if search_name == counter.name:
            print("This student is on the list")
            return
    print("This student is not on the list")
def get_student_address(search_name):
    for counter in list_of_homeroom_students:
        if counter.name == search_name:
            print(counter.address)
def get_student_basic_info(search_name):
    print("Getting information about this student")
    for counter in list_of_homeroom_students:
        if counter.name == search_name:
            print("Grade: ",counter.grade)
            print("ID: ",counter.ID)
            print("Address: ", get_student_address(search_name))
            print("Age: ", counter.age)
            print("Locker Number: ",counter.locker_number)
def list_homeroom_students():
    print("Now Showing The List Of Homeroom Students")
    for counter in list_of_homeroom_students:
        print(counter.name)

#MAIN CODE
while True:
    print("What would you like to do:")
    print("1:   View Homeroom Roster")
    print("2:   Add student to homeroom")
    print("3:   Remove student from homeroom")
    print("4:  Get a student's ID number")
    print("5:  See number of students in homeroom")
    print("6:  See basic student information")
    print("7:  See if a student is on the homeroom list")
    print("8:  Exit Program")
    try:
        choice = int(input("->)"))
        if choice == 1:
            #See list of students
            list_homeroom_students()
        elif choice == 2:
            #Add students to homeroom
            add_to_homeroom()
        elif choice == 3:
            #Remove stduents from homeroom
            pass
        elif choice == 4:
            #Gets a student's ID number
            pass
        elif choice == 5:
            #Get number of Homeroom Students
            print("Getting number of Homeroom Students")
            print(get_number_of_students())
        elif choice == 6:
            #See basic info about a student
            pass
        elif choice == 7:
            #Search the Roster to see if a student is on it
            print("What student do you want to search?")
            search_name = input("->")
            search_list_for_student(search_name)
        elif choice == 8:
            #Quit Program
            print("You have successfully exited the program")
            break
        else:
            print("An error has occurred, please try again")
    except:
        print("Please use a valid number")

print("Thanks for using the homeroom software")
