print("Program Started!")
print("Please enter a standard character:")

char = input()
asc = ord(char)

print(f"The ASCII code for {char} is {asc}")
print("Program ended!")


print("Program Started!")
print("Please enter an ASCII code:")

number_conv = abs(int(input()))
num = chr(number_conv)

if number_conv in range(32, 127):
    print(f"The character presented by the ASCII code {number_conv} is {num}")

print("Program Ended!")
