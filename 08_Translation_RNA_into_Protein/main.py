def get_codon_table():
    table = {}
    with open('./codon_table.data') as file:
        for entry in file:
            rna_codon, amino_acid = entry.strip().split()

            # Replace stop with newline
            if amino_acid == 'Stop':
                amino_acid = '\n'

            table[rna_codon] = amino_acid
    return table

codon_table = get_codon_table()
def rna_to_amino_acid(rna):
    mapped_rna = [codon_table[rna[i:i+3]] for i in range(0, len(rna), 3)]
    return ''.join(mapped_rna)

if __name__ == '__main__':
    rna = ''
    with open('./rosalind_prot.txt') as file:
        rna = file.readline().strip()
    
    amino_acid = rna_to_amino_acid(rna)

    print('{}'.format(amino_acid))