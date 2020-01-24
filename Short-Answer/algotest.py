


sum = 0

def testlog(n):
    global sum
    for i in range(n):
        print('i: ', i)
        j = 1
        while j < n:
            j *= 2
            print('j: ', j)
            sum += 1
    return sum


# print(testlog(15))


def bunnyEars(bunnies):
    print('bunnies: ', bunnies)
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies - 1)


# print(bunnyEars(800))

