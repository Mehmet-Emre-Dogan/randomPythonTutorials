############### Description - Purpose ###############
""" Assigning elements to a python list"""
#####################################################

def alternative1():
    print("\n\n" + "Alternative 1".center(50, "-") + "\n")
    myArr = []
    print(myArr)

    for i in range(3):
        myArr.append(None)
    print(myArr)

    for i in range(3):
        myArr[i] = input(f"Enter {i}th element: ")
    print(myArr)

def alternative2():
    print("\n\n" + "Alternative 2".center(50, "-") + "\n")
    myArr = [None]*3
    print(myArr)

    for i in range(3):
        myArr[i] = input(f"Enter {i}th element: ")
    # Proof of that we can append more items than the pre-initialized value (3).
    myArr.append(input("Last element: "))
    # End of proof.
    print(myArr)

def bestAlternative(): # For me, of course. This idea is subjective.
    print("\n\n" + "Best Alternative".center(50, "-") + "\n")
    myArr = []
    for i in range(3):
        myArr.append(input(f"Enter {i}th element: ")) 
    print(myArr)

alternative1()
alternative2()
bestAlternative()
