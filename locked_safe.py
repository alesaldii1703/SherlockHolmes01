# Sherlock Holmes has discovered a locked safe containing valuable information.
# Complete the code to unlock the safe.

import random

# Initialize variables
correct_code = "221B"  # The correct code to unlock the safe
attempts = 3
successful_attempts = 0
failed_attempts = 0

# Attempt to unlock the safe
while attempts > 0:
    print(f"\nAttempts remaining: {attempts}")
    guess = input("Enter the code to unlock the safe: ")

    # Check the guess
    if guess == correct_code:
        print("The safe is unlocked! Valuable information retrieved.")
        successful_attempts += 1
        break
    else:
        print("Incorrect code. Try again.")

        # Provide clues for the next attempt
        clue_position = random.randint(0, 3)
        clue_digit = correct_code[clue_position]
        print(f"Clue: The digit at position {clue_position + 1} is {clue_digit}.")

        failed_attempts += 1
        attempts -= 1

# Report the outcome
if successful_attempts > 0:
    print(f"Sherlock Holmes successfully unlocked the safe in {successful_attempts} attempt(s).")
else:
    print(f"Sherlock Holmes was unable to unlock the safe after {failed_attempts} failed attempt(s). Further clues are needed.")
