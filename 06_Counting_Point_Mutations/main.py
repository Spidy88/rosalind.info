def count_point_mutations(entry1, entry2):
    size = len(entry1)
    mutations = 0

    for i in range(size):
        if entry1[i] != entry2[i]:
            mutations += 1

    return mutations

if __name__ == '__main__':
    entry1 = ''
    entry2 = ''

    with open('./rosalind_hamm.txt') as file:
        entry1 = file.readline().strip()
        entry2 = file.readline().strip()

    point_mutations = count_point_mutations(entry1, entry2)

    print('{}'.format(point_mutations))
