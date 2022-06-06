#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      raj
#
# Created:     03-06-2022
# Copyright:   (c) raj 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
start = int(input("Enter the lower bound: "))
stop = int(input("Enter the upper bound: "))
print("Prime numbers between", start, "and", stop, "are:")
for val in range(start, stop):
  if val > 1:
    for i in range(2, val):
      if (val % i) == 0:
        break
    else:
      print(val, end=" ")