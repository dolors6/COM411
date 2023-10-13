driving = input ("Do you want to drive? yes/no")
if driving == "yes" :

    print ("Enter your age:")

    age = int(input())

    if age >= 18 and age < 60:
        print("You are eligible to drive!")
    elif age >= 60:
        print("You are too old to drive")
    elif age == 17:
        print("You can drive but there needs to be an adult to accompany you... Hey and don't forget your provisional!")

    else :
        print(f"You are too young to drive because you don't meet the requirements, {age} is too young!")


print("That's it!")
