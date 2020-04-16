phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
# pop off the last four objects from plist
for i in range(4):
    plist.pop()
plist.pop(0)  # get rid of the D
plist.remove("'") # remove the ' from plist

# Swap the two objects at the end of the list by first popping each object
# from the list, then using
# the popped objects to
# extend the list. This is a
# line of code that you’ll
# need to think about for a
# little bit. Key point: the
# pops occur *first* (in
# the order shown), then
# the extend happens.
plist.extend([plist.pop(),plist.pop()])

# This line of code pops the space from the
# list, then inserts it back into the list at
# index location 2. Just like the last line of
# code, the pop occurs *first*, before the
# insert happens. And, remember: spaces are
# characters, too.
plist.insert(2, plist.pop(3))
# Turn “plist” back into a string.
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
