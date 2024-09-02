# Lists

my_list = list((1, True, 'Hello', [11, 22, 33])) # Same form

# Show all list methods
# print(dir(my_list))

# Range List auto
list_range = list(range(1, 20))

# Favorite methods
print(my_list[-2]) # Show inverse
print(len(my_list))
print('Hello' in my_list) # Exist?
my_list[0] = 12 # Set value
my_list.append('text') # Insert
my_list.extend(['text_1', 'text_2', 'text_3']) # Insert many
my_list.insert(2, 'INTRUSO') # Insert in position
my_list.pop() # Delete last element
my_list.pop(-2) # Delete index element
my_list.remove('Hello') # Remove specific
my_list.clear() # Delete all

elements = [32, 16, 82, 9, -2]
elements.sort() # One type data list
elements.sort(reverse=True) # Reverse action
print(elements.index(9)) # Index