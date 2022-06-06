#-------------------------------------------------------------------------------
# Name:        module8
# Purpose:
#
# Author:      raj
#
# Created:     03-06-2022
# Copyright:   (c) raj 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def calculation(first,second,operator):
    first=input("enter the first number:")
    second=input("enter the second number:")
    operator=input("choose one of these +,-,/,* :")
    first =int(first)
    second=int(second)

    if operator=="+":
       calculation=print(first + second)
    if operator=="-":
       calculation=print(first - second)
    if operator=="*":
        calculation=print(first*second)
    if operator=="/":
        calculation=print(first/second)

print(calculation(9,3,"/"))
