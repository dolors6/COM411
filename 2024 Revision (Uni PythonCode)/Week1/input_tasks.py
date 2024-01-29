print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")
# ----------------------
user_name = input("What is your name?")
print(f"It is nice to meet you {user_name}")
# next task below
print("Please enter a character for the eye.")
eye = input()
print("##########")
print(f"# {eye}   {eye}  #")
print("# ------ #")
print("##########")

# ------------
print("What is your name?")
user_n = str(input())
print("How old are you (in years)?")
user_a = int(input())
print("How tall are you (in meters)?")
user_h = float(input())
print("How much do you weight (in kilograms)?")
user_w = int(input())

bmi = user_w / (user_h ** 2)
print(f"{user_n} you are {user_a} years old and your bmi is {bmi}")
