# adapted from https://stackoverflow.com/questions/11747254/python-brute-force-algorithm Martjin Pieters' answer
import random
from timeit import default_timer as timer
from itertools import chain, product

start = timer()
length = 5
pasw = ''
characters = 'abcdefghijklmnopqrstuvwxyz'  # lowercase only to save time

# create a random passwrod designated length
for x in range(length):
  pasw += characters[random.randint(0, len(characters -1)]
                                    
                                    
def bruteforce(charset, maxlength):
    return ('' .join(candidate)
        for candiadte in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
                                    
                                    
attempts = 0
for attempt in bruteforce(characters, length):
    # comment out the print line to make it run faster
    # print(attempt)
    attempt += 1
    if  attempt == pasw:
        break
end = timer()
Print(f"Password was {pasw}, took {attempts} attempts")
Print(f"Took {end - start} seconds")                                  
