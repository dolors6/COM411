print("What type of book if this?")
book_type = input()

if book_type == 'adventure':
    print(f"i like {book_type} books!")

print("Finished reading book.")
# ______________________________--

print("Please enter the activity to be performed.")
activity = input()

if activity == 'calculate' or activity == 'Calculate':
    print("Performing calculations...")

print("Activity completed!.")

#_____________________________--

print("Towards wnich direction should i go (up, down, left or right)?")
dir = input()

if dir == 'up' or dir == 'Up':
    print("I am moving in an upward direction!")
elif dir == 'down':
    print("I am moving in an downward direction!")
elif dir == 'left':
    print("I am moving towards the left direction!")
elif dir == 'right':
    print("I am moving towards the right!")
else :
    print("I am not moving nowhere!")
# -----------------------------------------

print("Please enter a whole number.")
num = int(input())

if num % 2 == 0:
    print("even number")
else:
    print("odd number")
#__________________________---

f_n = int(input("Please enter the first number."))
s_n = int(input("Please enter the second number."))

if f_n > s_n:
    print("The second number is the smallest")
elif f_n == s_n:
    print("both numbers are equal")
else:
    print("The first number is the smallest.")
# __________________________________________
