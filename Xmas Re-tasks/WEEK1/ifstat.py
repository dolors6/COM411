ride = input("Do you want to go on rides? y/n")

if ride == "y":
    age = int(input("For you to be able to go on this ride you must be over 18, How old are you?"))

# age >= 18 and age < 60:

    if 60 > age >= 18:
        print(f"You are good to enter the ride after all you are {age}")
    elif age == 61:
        print(f"{age} you are getting old you gezza lol, count your days..")
    elif age >= 17:
        print("Only accompanied by adults")
    else:
        print(f"You are {age} unfortunately you are not suited for this ride!")
else:
    print("Okay")
print("Done!")
