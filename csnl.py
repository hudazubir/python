#----------This is a CONDITION STATEMENT !!!!-------------
#----------and LOOPS !!!!-------------

#Condition statement - if, elif, else. 
#Make decision in source code based on certain conditions.
print("INI ADALAH CONDITION STATEMENT!")

#Get user's age #enter age using input. and input converted to an int using 'int()'
age = int(input("Enter your age: ")) 

#Check age using conditional statements
if age < 18: #age is less than 18
    print("You are a minor! Dasar BUDAKKK")
elif age >= 18 and age < 65: #between 18 and 65
    print("You are an adult !! CIEYYY DAH BESAR")
else: #selain dari dua di atas. 
    print("You are a senior citizen ^_^")


#----------------and LOOPS !!!!-----------------

#Loops - for and while. Used to execute a block of code repeatedly. 
#For = used when want to iterate over a sequence (list/tuple/range) specific number of times
print("INI ADALAH LOOPING !!")
print ("untuk FOR LOOP")
#Print number from 1-5 using for a loop
for i in range (1,6): #The range fx generates num from 1-5 (inclusive of 1, exclusive of 6).
    print(i)

#While = when u want to repeatedly execute a block of code as long as a condition is true. 
print("Untuk WHILE LOOP")
#Print number form 1-5 using a while loop
count = 10
while count <= 15:
    print(count)
    count += 1