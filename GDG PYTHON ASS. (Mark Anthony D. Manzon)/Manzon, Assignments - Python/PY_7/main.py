
# To catch error if the txt file name is incorrect
try:

# Call the filename as read mode 'r'
    with open('sample.txt', 'r') as file:
        sample = file.read()
        print("\nContents of the file:")
        print(sample) # Print the contents of the text file
        file.close()

# If the file name is not match
except FileNotFoundError:
    print("\nFile cannot be found\n")

# Make a new txt file and do it as write mode
with open('newfile.txt', 'w') as file:
        file.write("This is a new file, like New Year New Me XD\n") # You'll put the content here 
        print("New file created with content:")
        file.close()

with open('newfile.txt', 'r') as file:
        new_Content = file.read();
        print(new_Content) # The empty new txt file gets filled with the write("...")
        file.close()
        

# Using append 'a' to show how it adds new content to an existing txt file
with open('newfile.txt', 'a') as file:
        file.write("New line in the newfile.txt\n")
        print("New line using append 'a':")
        file.close()

with open('newfile.txt', 'r') as file:
        append = file.read()
        print(append)
        file.close()