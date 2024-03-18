print("Welcome to the Grade Calculator!")
print("This takes a grade on an assignment and tells you if you failed or not.")
print("Enter the total number of points available")
points_available = int(input("->"))
print("Enter the number of points earned")
points_earned = int(input("->"))
grade = (points_earned/points_available)*100
print(grade, "%")
if grade >= 60:
    print("You Passed!")
else: 
    grade < 60
    print("You failed!")
