def count_nucleotides(dna):
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0

    for letter in dna:
        if letter == 'A':
            count_a += 1
        elif letter == 'C':
            count_c += 1
        elif letter == 'G':
            count_g += 1
        elif letter == 'T':
            count_t += 1
        else:
            raise Exception('Can only count nucleotides A-C-G-T but encountered {}'.format(letter))
    
    return count_a, count_c, count_g, count_t

if __name__ == '__main__':
    dna = input('Enter a DNA sequence: ')
    
    a, c, g, t = count_nucleotides(dna)

    print('{} {} {} {}'.format(a, c, g, t))