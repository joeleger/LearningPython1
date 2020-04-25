import pprint
product = {'Book': 49.99,
           'PDF': 43.99,
           'Video':199.99,}

#no sort
print('no sort')
for k in product:
    print(k, '->', product[k])
print()
# sort by key
print('sort by key')
for k in sorted(product):
    print(k, '->', product[k])
print()
# sort by value
print('sort by value')
for k in sorted(product, key=product.get):
    print(k, '->', product[k])
print()
# sort by value reversed
print('sort by value reverse')
for k in sorted(product, key=product.get, reverse=True):
    print(k, '->', product[k])
print()

