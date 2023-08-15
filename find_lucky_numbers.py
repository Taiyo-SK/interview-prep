### Given an integer, n, return a list containing n unique random numbers between 1010, inclusive.
### i.e. do not repeat any numbers in the returned list.
### Assume n will never be < 0 or > 10.

### example
## input: 2, output: [3, 7]

## input: 0, output []

## if you ask for the max amount of numbers (10), your results should be 1-10 (randomized).

import random

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    nums = list(range(1, 11)) # generates a list of 1-10
    lucky_nums = [] # the output

    # for i in range(n):
    for i in range(n):
        random_num = random.choice(nums)
        print(random_num) # check what the random number is
        nums.remove(random_num)
        print(nums) # check that the random number has been removed from the originally collection
        lucky_nums.append(random_num)
        print(lucky_nums) # check to see what the list has become

    return lucky_nums
        

test_1 = 4
test_2 = 0
test_3 = 10

lucky_numbers(test_1)
# lucky_numbers(test_2)
# lucky_numbers(test_3)