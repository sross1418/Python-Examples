
def isprime(x):
  if x <= 0:
    return False
  if x== 2:
    return True
  if x % 2 == 0:
    return False
  for i in range(3, x, 2): #range(start, end, step)
    print(f"Dividing {x} by {i}, the remainder was {x % i}")
    if x % i == 0: #if the number is divisible by any number
      print(f"{x} was divisble by {i}, so itis not prime")
      return False #in the range up to itslef, it is not prime
    Print(f"{x} was found to be prime")
    return True
  

numList = range(1,251)
resultFile = open("results.txt", "w")
# for every number from 1 to 250
# if it's prime, -> find out how to tell if a number is prime or not -> is it divisble by any number? -> iterate through every number  from 3 to whatever the number was to see if it was dvisible by any of them, if it is, it's not prime (return False), if it's not, it is prime (return true), 1 and 2 are special cases
# write it to the file
for num in numList:
  if isPrime(num) == True:
    resultFile.write(str(num) + "\n")
resultFile.close()
Print("done")
