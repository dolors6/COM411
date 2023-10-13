print("How many apples should i remove?")

apple = int(input())
count = 1
while count <= apple:
    print("Removed apple.")
    count += 1

#First Task

print("How many obstacles must i avoid?")
obstacle = int(input())
count = 1
while count <= obstacle:
    print (f"Avoiding... Done! {count} obstacles avoided.")
    count += 1

#second task

print("All obstacles have been avoided.")

#third task

print("How many bars should be charged?")
bars = int(input())
count = 1

while count <= bars:
    print(f"Charging: {' █ ' * count}")
    count += 1

print("The battery is fully charged.")

print("Calculating the sum of the first 100 numbers...")
count = 1
final = 100
answer = 0
while count <= final:
    answer += count
    count += 1

print(f"Done! The answer is {answer}.")