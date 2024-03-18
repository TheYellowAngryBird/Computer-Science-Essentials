print("Welcome to the Letter Grade Calculator!")
print("This takes a grade on an assignment and tells you your letter grade on said assignment.")
print("Enter the total number of points available")
points_available = int(input("->"))
print("Enter the number of points earned")
points_earned = int(input("->"))
grade = (points_earned/points_available)*100
print(grade, "%")
if grade == 100:
    print("You earned an A+!")
elif grade >= 90:
    print("You earned an A!")
elif grade >= 80:
    print("You earned a B!")
elif grade >= 70:
    print("You earned a C!")
elif grade >= 60:
    print("You earned a D!")
else: 
    grade < 60
    print("You earned an F!")
