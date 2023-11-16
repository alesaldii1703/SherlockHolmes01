# Sherlock Holmes is investigating a crime scene. Watson provides information about the evidence.
# Use multiple accumulators and counters to gather information and draw conclusions.

# Initialize accumulators and counters
fingerprints = 0
footprints = 0
documents = 0
suspicious_persons = 0

# Ask Watson for information about the evidence
found_something = input("Watson, have you found any evidence? (yes/no): ").lower()

while found_something == 'yes':
    evidence_type = input("What type of evidence have you found? (fingerprint/footprint/document/suspicious person): ").lower()

    if evidence_type == 'fingerprint':
        fingerprints += 1
    elif evidence_type == 'footprint':
        footprints += 1
    elif evidence_type == 'document':
        documents += 1
    elif evidence_type == 'suspicious person':
        suspicious_persons += 1
    else:
        print("Invalid input. Please enter a valid type of evidence.")

    found_something = input("Watson, have you found anything else? (yes/no): ").lower()

# Draw conclusions based on the gathered information
print("\nInvestigation Report:")
print(f"Number of fingerprints found: {fingerprints}")
print(f"Number of footprints found: {footprints}")
print(f"Number of documents analyzed: {documents}")
print(f"Number of suspicious persons observed: {suspicious_persons}")

# Make deductions based on the evidence
if fingerprints > 0 and footprints > 0 and documents > 0:
    print("Sherlock Holmes deduces a complex plot involving multiple individuals.")
elif fingerprints == 0 and footprints == 0 and documents == 0:
    print("The investigation yields no significant evidence.")
else:
    print("Holmes gathers valuable information, but the full picture remains elusive.")
