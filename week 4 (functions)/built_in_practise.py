print("Program Started!")
print("Please enter a letter:")

usr = input()
conv = ord(usr)
print(f"The ASCII code for the {usr} is {conv}")
print("Program Ended!")


#now moving unto task 2

print("Program Started!")
print("Please enter an ASCII code:")

urm = abs(int(input()))
if urm in range(32, 127):
    letter = chr(urm)

    print(f"The character represented by the ASCII code {urm} is {letter}")
else:
    print("re-enter your input:")

print("Program Ended!")
