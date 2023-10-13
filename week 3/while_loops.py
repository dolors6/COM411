print("How many apples should i remove?")

apple = int(input())
count = 1
while count <= apple:
    print("Removed apple.")
    count += 1

print("How many obstacles must i avoid?")
obstacle = int(input())
count = 1
while count <= obstacle:
    print (f"Avoiding... Done! {count} obstacles avoided.")
    count += 1

print("All obstacles have been avoided.")