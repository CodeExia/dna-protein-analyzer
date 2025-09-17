import sys

#THE GC COMPUTATION IS BROKEN FIX IT

amino_acids = [0,0,0,0]

# Computing G and C percentage
def gc_computation(sequence = "", size = 0):
    gc_count = sequence.count("G") + sequence.count("C")
    percentage = (gc_count/size) * 100
    return round(percentage, 2)

# Computes the amino/base acid composition
def amino_acid_computation(sequence = "", size = 0, temp_array=None):
    for base in sequence:
        if base == "A":
            temp_array[0] += 1
        elif base == "T":
            temp_array[1] += 1
        elif base == "G":
            temp_array[2] += 1
        elif base == "C":
            temp_array[3] += 1

# Error checking for the file path
if len(sys.argv) < 2:
    print("Please provide a FASTA/FASTAQ file")
    print("Usage: python mainscript.py \"filename\"")
    sys.exit(1)
else:
    fasta_file = open(sys.argv[1], 'r')

# Reading the header
# Ignore '>'
header = fasta_file.readline()
print("Header: ", header[1:])

# Reading the DNA sequence
dna = fasta_file.read()

# Sequence length
length = len(dna)
print("Sequence length: ", length)

# GC printing
print("GC composition percentage: ", gc_computation(dna, length),"%")

# Amino/base acid composition
amino_acid_computation(dna, length, amino_acids)
print("Base/amino acid composition: ")
print("Adenine = %d %f\nGuanine = %d %f\nCytosine = %d %f\nThymine = %d %f\n" % (amino_acids[0],round(((amino_acids[0]/length)*100), 2), amino_acids[1],round(((amino_acids[1]/length)*100), 2), amino_acids[2],round(((amino_acids[2]/length)*100), 2), amino_acids[3], round(((amino_acids[3]/length)*100), 2)))

fasta_file.close()
