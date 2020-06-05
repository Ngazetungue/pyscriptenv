# This program displays ten random
# numbers in the range of 1 through 50.

import random

def randomNumber():
      for count in range ( 10 ) :
# Get a random number.
            number = random.randint(1, 50)
# Display the number.
            print (number)
# Call the randomNumber function
randomNumber()
