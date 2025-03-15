
# List of original items
orig_Dictionary = {'name' : 'Mark Anthony', 'age' : 19}
print("\nOriginal Dictionary:\n", orig_Dictionary, "\n")

# Adding a new value to the list
orig_Dictionary['city'] = 'Quezon City'
orig_Dictionary['current grade level'] = '1st year college'
print("Dictionary afte adding an item:\n", orig_Dictionary, "\n")

# Updating an item in the list
orig_Dictionary['city'] = 'Calamba City'
print("Dictionary after updating an item:\n", orig_Dictionary, "\n")

# orig_Dictionary.pop('city')
# Deleting an item from the list
del orig_Dictionary['age']
print("Dictionary after deleting an item:\n", orig_Dictionary, "\n") 

