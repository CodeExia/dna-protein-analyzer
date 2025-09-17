# Given DNA sequence
sequence = "ATGCGTATCGATCGATCGGCTTAGCTAGCTAGCTAGCATCGATCGATGCTAGCTAGCTA"

# Counting occurrences of each base
base_counts = {
    "A": sequence.count("A"),
    "T": sequence.count("T"),
    "C": sequence.count("C"),
    "G": sequence.count("G")
}

# Calculating total length
total_length = len(sequence)

print(base_counts)
print("Total length of the sequence:", total_length)
