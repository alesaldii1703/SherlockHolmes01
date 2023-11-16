# Sherlock Holmes is on a new adventure to recover a stolen ruby. Little does he know, the culprit might be closer than he thinks.

print("Sherlock Holmes is on the trail of a stolen ruby, rumored to be hidden in a mysterious location.")
print("Holmes follows the clues to a remote village where strange occurrences have been reported.")

# Investigate the village
print("\nAs Holmes explores the village, he encounters various suspects:")
print("1. The innkeeper, Mrs. Hudson.")
print("2. The local artist, Vincent van Holmes.")
print("3. The eccentric scientist, Professor Moriarty.")
print("4. The humble turkey, named Red.")

# Interrogate the suspects
suspect = input("\nHolmes, who would you like to interrogate first? (Enter the suspect's number): ")

if suspect == '1':
    print("\nMrs. Hudson denies any involvement in the theft and claims she knows nothing about the ruby.")
elif suspect == '2':
    print("\nVincent van Holmes insists he was busy painting and had no time for theft.")
elif suspect == '3':
    print("\nProfessor Moriarty, though suspicious, denies any wrongdoing.")
elif suspect == '4':
    print("\nHolmes approaches the humble turkey, Red. The turkey seems unusually calm.")

    # Search the surroundings
    search_area = input("Holmes, where would you like to search for the ruby? (Enter a location, e.g., garden): ")

    if search_area.lower() == 'garden':
        print("\nIn a surprising twist, Holmes discovers the stolen ruby hidden beneath the feathers of the unsuspecting turkey, Red!")
        print("It seems the turkey was the unlikely thief all along.")

# Conclude the adventure
print("\nThe mystery of the stolen ruby is solved! Holmes apprehends the turkey, Red, and recovers the precious gem.")
print("Another peculiar case closed by the brilliant detective.")
