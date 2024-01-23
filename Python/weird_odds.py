'''
Given an integer, n, perform the following conditional actions:
    If n is odd, print "Weird".
    If n is even and in the inclusive range of 2 to 5, print "Not Weird".
    If n is even and in the inclusive range of 6 to 20, print "Weird".
    If n is even and greater than 20, print "Not Weird".
'''

import random

n = random.randint(1, 100)
print(n)

if __name__ == '__main__':
    # n = int(input().strip())
    # for n in range(1,101):
    if (n%2 != 0) or (n%2 == 0 and (n in range(6,21))):
        print("Weird")
    else:
        print("Not Weird")
