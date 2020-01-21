

# Advanced Sets

s = set()
s.add(1)
s.add(2)
s.add(1)

s_copy = s.copy()
s_copy.add(4)

s_diff = s_copy.difference(s)

st = {1,3,4}

print(s)
print(st)

s_union = s.union(st)
print(s_union)


s_union = s.intersection(st)
print(s_union)

# print(s_diff)

# print(s_copy)

# print(s)




