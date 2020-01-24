


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


# Suppose that you have an n-story building and 
# plenty of eggs. Suppose also that an egg gets broken 
# if it is thrown off floor f or higher, and doesn't 
# get broken if dropped off a floor less than floor f. 
# Devise a strategy to determine the value of f such 
# that the number of dropped + broken eggs is minimized.

# Write out your proposed algorithm in plain English 
# or pseudocode AND give the runtime complexity of 
# your solution.
