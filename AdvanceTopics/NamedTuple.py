# Difference between normal and NamedTuple is indexing

# Normal Tuple
t=(1,2,3,4)
print(t[0])

# Named Tuple
from collections import namedtuple


family = namedtuple('family','fisrt second third')

pacnic_party = family(fisrt='johnny', second='monny', third='tolly')

print(pacnic_party.fisrt)
print(pacnic_party.second)
print(pacnic_party.third)













