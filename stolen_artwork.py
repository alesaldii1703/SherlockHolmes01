# Sherlock Holmes is investigating the theft of valuable artwork. Solve the logic puzzle to identify the thief.

# Initialize variables
suspect_count = 3
stolen_art_count = 2

# Deductive reasoning
while stolen_art_count > 0:
    print(f"\nCurrent suspects: {suspect_count}")
    suspect = input("Holmes, who should we investigate next? (Enter suspect's name): ")

    if suspect == 'Moriarty':
        print("Moriarty is not the thief.")
    elif suspect == 'Watson':
        print("Watson is not the thief.")
    elif suspect == 'Adler':
        print("Adler is not the thief.")
    else:
        print("Invalid input. Please enter a valid suspect.")

    stolen_art_count -= 1

# Conclude the investigation
print("\nInvestigation Report:")
if stolen_art_count == 0:
    print("Sherlock Holmes deduces the thief successfully.")
else:
    print("The thief remains at large. Further investigation is needed.")
