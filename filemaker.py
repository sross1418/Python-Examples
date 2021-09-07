# filemaker.py
from datetime import date
import os
number = 1
DATE = date.today().strftime("%b-%d-%y") # save the date in month-day-year format asa a string
name = input ("What is your name? ")
directory - f" ./{name}-{Date}"
currentFile = name + str(number)
#echo currentFile
if os.path.isdir(directoy):
  print(f"{directory} already exist")
else:
  print(f"creating {directory}")
  os.mkdir(directory")
          
filesCreated = 0
while filesCreated < 25:
  if os.path.isfile(f{directory}/{currentFile}"):
    print(f"Creating {currentFile}")
    number +=1
    #print(number)
    #print(filesCreated
    currentFile = name + str(number)
 else:
    print(f"Creating {currentFile}")
    file = open(f"{directory/{currentFile}")
#os.system(f"{touch {directory/{curentFile}")
number += 1
currentFile = name + str(number)
