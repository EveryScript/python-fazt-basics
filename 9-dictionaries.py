# Dictionaries

book = {
    'name': 'Pirates of the caribean',
    'quantity': 12,
    'price': 12.99,
    'image': 'book.png',
    'premium': True
}

print(book.keys()) # Show keys
print(book.items()) # Show all items
book.clear() # Set empty dictionary
del book # Delete dictionary

books = [
    { 'name':'Wisdom in the forest', 'price':15.99, 'edition':'Firex'},
    { 'name':'Callie The hunter', 'price':16.99, 'edition':'Vallir' },
    { 'name':'Into the Darkness', 'price':19.99, 'edition':'Fazt' }
]

print(books)