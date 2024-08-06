#Example: Counting Down with a While Loop

#Get initial number from the user
initial_number = int(input("Enter a number to start the countdown: "))

#Validate input
if initial_number <= 0:
    print("Please enter a positive number.")
else:
    countdown = initial_number #Initialize countdown variable

    while countdown >= 1: #Use a while loop to count down and print
        print(countdown)
        countdown -= 1

    print("Countdown complete!")

