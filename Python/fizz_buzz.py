'''
Write a function that conditionally prints out the numbers from 1 to 100: 
For multiples of 3, it should print "Fizz" instead of the number.
For multiples of 5, it should print "Buzz" instead of the number.
If the number is a multiple of both 3 and 5, then it should output "FizzBuzz." 
'''

###> Function for single number input by user
def fizzybuzzy(n):
    for i in range(1, n+1):
        if ((i % 3) == 0) and ((i % 5) == 0):
            print('FizzBuzz')
        elif (i % 3) == 0:
            print('Fizz')
        elif (i % 5) == 0:
            print('Buzz')
        else:
            print(i)

# Example
num = int(input())
fizzybuzzy(num)



###> Function for defined sequence
import numpy as np
import pandas as pd

def fizzybuzzy(n_seq):
    if ((n_seq % 3) == 0) and ((n_seq % 5) == 0):
        return 'FizzBuzz'
    elif (n_seq % 3) == 0:
        return 'Fizz'
    elif (n_seq % 5) == 0:
        return 'Buzz'
    else:
        return n_seq

# Example
s = pd.Series(np.arange(1,101))
s.apply(fizzybuzzy)