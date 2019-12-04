def count_rabbits(afterMonths, perLitter):
    twoMonthsAgo = 1
    oneMonthAgo = 1

    rabbits = 1
    for _ in range(3, afterMonths + 1):
        rabbits += twoMonthsAgo * perLitter
        twoMonthsAgo, oneMonthAgo = oneMonthAgo, rabbits

    return rabbits

if __name__ == '__main__':
    n, k = input('Enter a number of months and rabbits per litter: ').split()
    
    rabbits = count_rabbits(int(n), int(k))

    print('{}'.format(rabbits))