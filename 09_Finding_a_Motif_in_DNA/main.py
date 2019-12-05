import re

def find_motifs(dna, motif):
    pattern = re.compile('(?={})'.format(motif))

    return [match.start()+1 for match in pattern.finditer(dna)]

if __name__ == '__main__':
    dna = ''
    motif = ''
    with open('./rosalind_subs.txt') as file:
        dna = file.readline().strip()
        motif = file.readline().strip()
    
    indexes = find_motifs(dna, motif)

    print(' '.join([str(index) for index in indexes]))