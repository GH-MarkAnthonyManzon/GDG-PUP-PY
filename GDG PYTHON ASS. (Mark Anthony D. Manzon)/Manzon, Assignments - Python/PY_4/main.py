
#Creating a function for the greeting message
def create_Greeting(name):

#Insert the message with the name parameter
    return f"Hello {name}, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

#Handling the exception
try:
    #Asks user the input their name
    name = input("Enter your name: ")

    #Strictly checks if the input is an alphabet (includes spaces Ex. John Christopher), or not (Numbers, Symbols)
    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError ("Invalid input: Please enter a valid name.") 

    #Calls the function and prints the greeting message
    greeting = create_Greeting(name)
    print(f"\nThe greeting message is:\n{greeting}")

#Prints the error message
except ValueError as error_Handler:
    print(error_Handler)
    