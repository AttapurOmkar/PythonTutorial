# Ordered sequence of objects
# my_list =[Object1,Object2,Object3]

my_list1=[1,2,3]
print(my_list1)

my_list2=["zero","one","two"]
print(my_list2)

# List concatenation
my_list3=my_list1+my_list2
print(my_list3)

my_list2.append('three')
print(my_list2)

# List compression
word='string'
my_list=[]
for letter in word:
    my_list.append(letter)
print(my_list)
print('x'*20)

listcol=[1,2,3,4]
list_com=[((letter**2)+2) for letter in listcol if letter in [1,2,3]]
print(list_com)

