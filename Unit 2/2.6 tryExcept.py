
#This file will demonstrate how to prevent crashes using 'try... except...'

#For Lesson 2.6, use this code to learn how try/except works.
#Then, based on what you learned, build your own code that uses try/except
#Or, you may update old code of yours to have a try/except
#START OF EXAMPLE
#print while True:

#print    try:
#print        first_num = float(input("Give me a number "))
#print        second_num = float(input("Give me another number "))
#print        answer = first_num + second_num
#print        print(first_num ,"+",  second_num, "is", answer)
#print        break
#print    except:
#print        print("You did not provide numbers! Please try again!")

#print print("Good Bye")
#END OF EXAMPLE
while True:

    try:
        first_num = float(input("What is the first value?"))
        second_num = float(input("What is the second value?"))
        third_num = float(input("What is the third value?"))
        fourth_num = float(input("What is the fourth value?"))
        fifth_num = float(input("What is the fifth value?"))
        average = (first_num + second_num + third_num +  fourth_num + fifth_num) / 5

        print("The average is ",average)
        break
    except:
        print("Invalid Values, please try again")



