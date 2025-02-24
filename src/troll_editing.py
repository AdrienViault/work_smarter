import datetime
import random
import os

# Get the current weekday (Monday=0, ..., Sunday=6)
today = datetime.datetime.today().weekday()
print(f"Today is {today}.")

# Calculate chances: (today + 1) chances out of 7
chances = today + 1
print(f"Allowed chances: {chances}.")

# Roll a random integer between 1 and 7 (inclusive)
roll = random.randint(1, 7)
print(f"Rolled a {roll}.")

if chances==7:
    print("It's Sunday, we'll randomize the chances.")
    chances = random.randint(1, 7)

def log_roll(roll_value, chances):
    # Ensure the directory exists
    log_dir = "data/troll_rolls"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "troll_roll.txt")
    
    # Append the roll value as a new line
    with open(log_file, "a") as file:
        # Write the daily value that random needs to surpass and random roll, then add a newline
        file.write(f"more than {chances} to continue and rolled {roll_value}\n")


# Log the roll number
log_roll(roll, chances)


# Check if the random roll falls within the allowed chances
if roll > chances:
    print("The roll is within the allowed chances.")
    print(f"Roll: {roll}, Chances: {chances}")
    # Create (or overwrite) the file with the content "True"
    with open("continue.txt", "w") as file:
        file.write("True")
    print("continue.txt created with 'True'.")
else:
    print("The roll is outside the allowed chances.")
    print(f"Roll: {roll}, Chances: {chances}")
    with open("continue.txt", "w") as file:
        file.write("False")
    print("continue.txt created with 'False'.")
