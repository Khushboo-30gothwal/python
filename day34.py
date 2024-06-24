# update method
ep1 = {122:34, 143:45, 240:56}
ep2 = {246:45, 567:78}

ep1.update(ep2)
print(ep1)
# clear() to clear all items from given dictionary
# ep1.clear()
# print(ep1)

# pop() to pop() an particular itms from dictionary
ep1.pop(122)
print(ep1)

# popitem() to pop() last item from given dictionary
ep1.popitem()
print(ep1)

# del to remove dictionary items
del ep1[240]#if key is given
print(ep1)
# if key is not given
del ep1
print(ep1)