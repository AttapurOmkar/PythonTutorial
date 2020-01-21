
numA = int(input("Please enter First Number = "))
numB = int(input("Please enter Second Number = "))
numC = int(input("Please enter Third Number = "))

try:

    if numA < numB and numA < numD :

        print(f"{numA} is smallest of {numB} and {numC}")

    elif numB < numA and numB < numC :

        print(f"{numB} is smallest of {numA} and {numC}")

    else:
        print(f"{numC} is smallest of {numA} and {numB}")

except:
    print("There is an error in the code")
    print("There is an error in the code")

else:

    Avg = (numA + numB + numC) / 2
    print(f" Avg of all three number is {Avg}")

finally:
    Square = (numA + numB + numC)**2
    print(f" Square of all three number is {Square}")
