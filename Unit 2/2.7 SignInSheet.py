fileName = "Sign-In_Sheet.txt"

def writeToFile(content):
    try:
        with open(fileName, 'a') as file:
            content = content + "\n"
            file.write(content)
            print("Content Added")
            file.close()
    except:
        print("An error has occurred, please try again")

def readFromFile():
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            print(content)
            file.close()
    except:
        print("An error has occurred, please try again")

while True:
    print("What would you like to do?")
    print("1: Sign-In   2: Read Sign-in Sheet   3: Sign-Out")
    choice = input("->")
    if choice == "1":
        print("What is your name?")
        content = input("->")
        writeToFile(content)
        print("Content added to file")

    elif choice == "2":
        print("Reading the sign-in sheet")
        readFromFile()

    elif choice == "3":
        #choice 3 closes the program using 'break' command
        print("You have successfully signed out")
        break
    else:
        print("An error has occurred, please try again")
print("Good Bye!")
