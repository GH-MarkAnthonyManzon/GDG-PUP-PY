
#Create a list of numbers
num_List = [27, 45, 18, 36, 9]
print("\nOriginal List:", num_List)

#Catch error inputs
try:
    
    #User input to add a number to the list
    add_List = int(input("Enter a number to add to the list: "))
    num_List.append(add_List)
    #Output after the added number
    print("\nList after adding an element:", num_List)

    #User input to remove a number from the list
    remove_List = int(input("Enter a number to remove from the list: "))
    #Conditional statement to check if the removed number is in the list
    if remove_List in num_List:
        #If true, number is removed from the list
        num_List.remove(remove_List)
        print("\nList after removing an element:", num_List)

        #If the number removed was true, it will sort the list
        num_List.sort()
        print("List after sorting:", num_List, "\n")
    else:
        #if false, program terminates and notify the user
        print(f"\n{remove_List} is not in the list.")
    
except ValueError:
    print("\nPlease enter a valid number.\n") #Only if the user inputs a non-number value