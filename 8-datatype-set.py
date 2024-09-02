# DataType "Set"

# --> Collection without index and without order

colors = { 'red', 'blue', 'orange'}
print('blue' in colors) # Exist in collection?
colors.add('violet') # Add element (first position default)
colors.remove('orange') # Delete element
# colors.clear() # Be empty
# del colors # Delete variable
print(colors)