# Practice with type() and isinstance()

student_age = 20
course_price = 4.50
student_name = "Yakob"
is_enrolled = True

print("Age:", type(student_age))
print("Price:", type(course_price))
print("Name:", type(student_name))
print("Enrolled:", type(is_enrolled))

print("Age is int:", isinstance(student_age, int))
print("Price is float:", isinstance(course_price, float))
print("Name is str:", isinstance(student_name, str))
print("Enrolled is bool:", isinstance(is_enrolled, bool))

print("Age is a number:", isinstance(student_age, (int, float)))