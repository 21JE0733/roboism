#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      raj
#
# Created:     03-06-2022
# Copyright:   (c) raj 2022
# Licence:     <your licence>
#-----------   --------------------------------------------------------------------

b=(input("choose one out of asc,desc and none :"))
NumList = []


Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
        value = int(input("Please enter the Value of %d Element : " %i))
        NumList.append(value)
if b=="asc":
        for i in range (Number):
         for j in range(i + 1, Number):

          if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print("Element After Sorting List in Ascending Order is : ", NumList)

if b=="desc":
   for i in range (Number):
      for j in range(i + 1, Number):
        if(NumList[i] < NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print("Element After Sorting List in desending  Order is : ", NumList)

if b=="none":
       print("Element is original list:",NumList)




