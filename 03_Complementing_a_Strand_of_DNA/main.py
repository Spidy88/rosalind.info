def complement_dna(dna):
    transform = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    mapped_dna = [transform[letter] for letter in reversed(dna)]
    return ''.join(mapped_dna)

if __name__ == '__main__':
    dna = input('Enter a DNA sequence: ')
    
    complement = complement_dna(dna)

    print('{}'.format(complement))