from datetime import datetime

while True:
    user_age = input("What is your age? ")

    # Check if the input is a numeric value
    if user_age.isdigit():
        # user_age <= 119
        user_age = int(user_age) # iand user_age <= 119

        # Calculate the birth year
        current_year = datetime.now().year
        birth_year = current_year - user_age

        print(f"You are {user_age} years old, which means you were born in the year {birth_year}.")
        break  # Exit the loop if the input is valid
    else:
        print("Invalid input. Please enter a valid numeric value for your age.")
