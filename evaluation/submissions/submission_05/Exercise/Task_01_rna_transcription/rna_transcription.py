def to_rna(dna_strand):
    complement = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    # Transcribe the DNA sequence to RNA
    rna_sequence = ''.join(complement[nucleotide] for nucleotide in dna_strand)
    return rna_sequence


# Example usage
DNA_input = "ACGTGGTCTTAA"
RNA_output = to_rna(DNA_input)
print("DNA Input:", DNA_input)
print("RNA Output:", RNA_output)
