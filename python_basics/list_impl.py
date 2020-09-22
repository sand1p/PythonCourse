# list declaration
student_grades: [str] = [7.8, 9.2, 10, 8.7]

print(student_grades)


# Method: It is associated with object
# Function: It is not associated with any object

sum = sum(student_grades)
length = len(student_grades)

avg = sum / length
print("average", avg)