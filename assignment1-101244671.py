
numStudents = 0
totalGrade = 0

def function():
    name = input("Please enter your first and last name:")
    names = name.split()
    first = names[0]
    last = names[1]
    grade = input("Please enter your grade:")
    numStudents += 1
    totalGrade += grade
    print(first + " " + last + " " + str(grade))
function()
averageGrade = totalGrade / numStudents
print("Grade average " + str(averageGrade))
