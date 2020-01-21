from collections import OrderedDict
# Ordered Dictionary

d1 ={}

d1["a"] = 1
d1["b"] = 2

print(d1)


d2 ={}
d2["b"] = 2
d2["a"] = 1

print(d2)

print(d1 == d2)

d1 = OrderedDict()

d1["a"] = 1
d1["b"] = 2

print(d1)


d2 = OrderedDict()
d2["b"] = 2
d2["a"] = 1

print(d2)

print(d1 == d2)

