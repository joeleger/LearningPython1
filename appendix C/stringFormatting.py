
price = 49.99
tag = "is a real bargain?"

# *****Concatenation
print("Concatenation")
msg = 'At ' + str(price) + ', Head First Python ' + tag
print(msg)
print()

# ****String formats (using the % syntax).
print('% syntax')
msg = 'At %2.2f, Head First Python %s' % (price, tag)
print(msg)
print()

# *****Using string’s format method
print('string’s format method')
msg = 'At {}, Head First Python {}'.format(price, tag)
print(msg)
print()
# examples https://docs.python.org/3/library/string.html#formatexamples