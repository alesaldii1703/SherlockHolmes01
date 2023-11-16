# Sherlock Holmes is solving a logic puzzle, but there are errors in the code.
# Your task is to identify and correct the errors to reveal the solution.

# Initialize suspects and clues
suspect_Moriarty = True
suspect_Watson = True
suspect_Adler = True
clues = 3

# Holmes eliminates suspects based on clues
while clues > 0:
    if suspect_Moriarty:
        suspect_Moriarty = False
    else:
        clues -= 1

    if suspect_Watson:  # Corrected the syntax error
        suspect_Watson = False
    else:
        clues -= 1

    if suspect_Adler:
        suspect_Adler = False
    else:
        clues -= 1

# Identify the remaining suspect
if suspect_Moriarty:
    culprit = "Moriarty"
elif suspect_Watson:
    culprit = "Watson"
elif suspect_Adler:
    culprit = "Adler"
else:
    culprit = "Unknown"

# The remaining suspect is the culprit
print(f"The culprit is {culprit}")
