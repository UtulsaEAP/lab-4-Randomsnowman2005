"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Mohamad Ali Fakhoury
Lab Time: Thurs @2pm

"""

import math
def reverse_binary():
    user_num = int(input())
    stri = ''
    while user_num > 0:
        stri = stri + str(user_num % 2)
        user_num = user_num // 2
       
    else: print(stri)

if __name__ == "__main__":
    reverse_binary()