#----------This is a VARIABLES !!!!-------------

#String variable
first_name = "Nurhuda" 
last_name = "Binti Zubir"
age = 24 #Int variable
student = True #Boolean variable

#The output
print ("My name is:", first_name, last_name, "and I am", age, "years old." )

#Can use variables in various ways, like printing their values, performing calculation, and more.
birth_year = 2000
current_year = 2024
age_calculation = current_year - birth_year
print("Calculated age:", age_calculation)

#variable scope - it can be accessed or modified (akses/ubahsuai)
def my_function():
    local_variable = "I'm local"
    print(local_variable)

my_function()        # Prints "I'm local"
#print(local_variable)  # Raises an error (local_variable not defined in this scope)

#Variable Reassignment - with new values as needed
count = 5
print(count)
count = count + 1
print(count)

#Constants (Pemalar) - programmer often use uppercase v.n to indicate that a variable's value should not be changed
PI = 3.14159
RADIUS = 5
area = PI * RADIUS ** 2
print("Area of the circle:", area)