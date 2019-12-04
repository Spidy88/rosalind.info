import re
gc_pattern = re.compile('[CG]')

def calculate_gc_content(dna):
    return len(gc_pattern.findall(dna)) / len(dna)

def find_highest_gc_content(entries):
    best = (None, -1)
    for entry in entries:
        gc_content = calculate_gc_content(entry[1])
        if gc_content > best[1]:
            best = (entry, gc_content)
    return best

if __name__ == '__main__':
    entries = []
    with open('./rosalind_gc.txt') as file:
        for line in file:
            if line[0] == '>':
                entries.append((line[1:].strip(), ''))
            else:
                last_entry = entries[-1]
                entries[-1] = (last_entry[0], (last_entry[1] + line).strip())

    highest_gc = find_highest_gc_content(entries)

    print('{}\n{}'.format(highest_gc[0][0], highest_gc[1]*100))