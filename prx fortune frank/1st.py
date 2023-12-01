# ask user for age.
# This time use (input) to print and collect data.
# name input variable

age_user = input("Enter your age : ")
age_user = int(age_user)

# Calculate the birth year

year_of_birth = 2023 - age_user

# if age_user
print(f"You were born in {year_of_birth}")
# else:
#    print("Re-enter input, Enter a valid number.")
#i need to use while loop to re-display the question, until the valid answer is given..
