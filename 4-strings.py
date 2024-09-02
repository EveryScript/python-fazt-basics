# Strings
phrase = 'welcome to energy'

# All methods of strings
# print(dir(phrase))

# Favorite methods
print(phrase.upper())
print(phrase.lower()) 
print(phrase.swapcase()) # Inverse case
print(phrase.capitalize()) # Title case
print(phrase.replace('energy', 'power'))
print(phrase.count('e'))
print(phrase.startswith('w')) # Case sense (W <> w)
print(phrase.endswith('gy')) # Case sense (Gy <> gy)
print(phrase.split('to'))
print(phrase.find('to'))
print(len(phrase))
print(phrase.index('n'))
print(phrase.isalpha())
print(phrase.isnumeric())
print(phrase[9]) # Left to right
print(phrase[-2]) # Right to left
print(f"This is interpolation of {phrase}")