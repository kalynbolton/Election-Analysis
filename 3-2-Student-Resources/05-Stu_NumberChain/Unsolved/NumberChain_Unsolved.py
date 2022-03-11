# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    loop_number = int(input("How many loops do you want to do? "))
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for num in range(0, loop_number + 1):
            print(num)

        # Print each number in the range
       

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")