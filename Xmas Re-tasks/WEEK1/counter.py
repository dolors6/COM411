num1 = input("Please enter the first whole number.")
num2 = input("please enter the second whole number.")
num3 = input("Please enter the third whole number.")

if not (num1.isdigit() and num2.isdigit() and num3.isdigit()):
    print("Please enter the correct value.")
else:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

even_amount = 0
odd_amount = 0

if num1 % 2 == 0:
    even_amount += 1
else:
    odd_amount += 1

if num2 % 2 == 0:
    even_amount += 1
else:
    odd_amount += 1

if num3 % 2 == 0:
    even_amount += 1
else:
    odd_amount += 1

print(f"There were {even_amount} even and {odd_amount} odd numbers.")
