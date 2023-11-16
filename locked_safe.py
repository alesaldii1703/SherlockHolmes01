# Sherlock Holmes has discovered a locked safe containing valuable information. Complete the code to unlock the safe.

# Initialize variables
code = ""
attempts = 3

# Attempt to unlock the safe
while attempts > 0:
    print(f"\nAttempts remaining: {attempts}")
    guess = input("Enter the code to unlock the safe: ")

    # Check the guess
    if guess == "221B":
        print("The safe is unlocked! Valuable information retrieved.")
        break
    else:
        print("Incorrect code. Try again.")
        attempts -= 1

# Report the outcome
if attempts == 0:
    print("Sherlock Holmes was unable to unlock the safe. Further clues are needed.")
