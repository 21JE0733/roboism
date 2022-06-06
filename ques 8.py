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

def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit

print(sum_digits_string("123abcd45"))
print(sum_digits_string("abcd1234"))