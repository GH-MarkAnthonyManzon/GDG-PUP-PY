

try:

    # Get the user's age
    userAge = int(input("Enter your age: "))

    # Check if the user's input is negative
    if userAge < 0:
        print("Your age cannot be negative!")
    
    # Process to validate the user's age
    elif userAge < 13:
        print("You are a child")
    elif userAge < 20:
        print("You are a teenager")
    elif userAge < 60:
        print("You are an adult")

    # If the user's age exceeds 60    
    else:
        print("You are a senior citizen") 

except ValueError:
    print("Please enter a valid number")

# Try and except, to do error handling