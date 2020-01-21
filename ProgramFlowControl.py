#if elif else
post="home"

if post=="home":
    print("this is not post")
elif post=="bank":
    print("this is bank")
else:
    print("I am in else")

# For loops
var_itr=[1,2,3,4]

for item_var in var_itr:
    print(item_var)

# While loop runs a piece of code until it meets a given condition
x=0
while x<5:
    print(f"The current value of {x}")
    x += 1

#Break
#Continue
#Pass