
#Part 1:
#for loop

#Array list for favorite foods
fav_Foods = ["Lomi", "Adobo", "Bicol Express", "Kare-kare", "Binagoongan"]

print("My favorite foods are:")

#For loop to automate the process
for foods in fav_Foods:
    #Print formatting for that bulleted list of favorite foods
    print(f"- {foods}")

print("\n") #New line to give space between the two parts of the program


#Part 2:
#while loop

#try and except to handle those invalid inputs
try:

    #User input for the countdown
    starting_Number = int(input("Enter a positive number to start the countdown: "))

    #Condition for the countdown
    if starting_Number <= 0:
        print("Invalid input. Please enter a number greater than zero.")
    else:
        print("Countdown:")

    #Loop for the countdown to trigger
        while starting_Number > 0:
            print(starting_Number)
            starting_Number -= 1
        
        print("Countdown complete!") #Notify that the countdown is done

#Program will stop if user inputs negative numbers or letters/symbols
except ValueError:
    print("Invalid input. Please enter a positive integer.")