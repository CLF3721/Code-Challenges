'''
Write a function that conditionally prints out the numbers from 1 to 100: 
For multiples of 3, it should print "Fizz" instead of the number.
For multiples of 5, it should print "Buzz" instead of the number.
If the number is a multiple of both 3 and 5, then it should output "FizzBuzz." 
'''

###> Loop
for (i in 1:100){
  if(i%%3 == 0 & i%%5 == 0) {
    print('FizzBuzz')
  }else if(i%%3 == 0){
    print('Fizz')
  }else if (i%%5 == 0){
    print('Buzz')
  }else{
    print(i)
  }
}


###> Function for num sequence
fizzybuzzy <- function(n_seq){
  if(n_seq%%3 == 0 & n_seq%%5 == 0) {
    print('FizzBuzz')
  }else if(n_seq%%3 == 0){
    print('Fizz')
  }else if (n_seq%%5 == 0){
    print('Buzz')
  }else{
    print(n_seq)
  }
}

# apply it to the numbers 1 to 100
sapply(seq(from=1, to=100, by=1), fizzybuzzy)