import json
import time
import random

def choose_number():
    # Load the existing numbers from the JSON file
    with open('numbers.json', 'r') as f:
        numbers = json.load(f)
    
    # Generate a random number between 1 and 183
    number = random.randint(1, 183)
    
    # Check if the number is in the last 30 numbers
    while number in numbers[-30:]:
        print("The same number", number, "was chosen again.")
        number = random.randint(1, 183)  # Generate another number if it's in the last 30
    
    # Add the chosen number to the list
    numbers.append(number)
    
    # Save the updated list back to the JSON file
    with open('numbers.json', 'w') as f:
        json.dump(numbers, f, indent=4)
    
    return number
if __name__ == "__main__":
    chosen_number = choose_number()
    print("Chosen number:", chosen_number)