"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Mohamad ali Fakhoury
Lab Time: Thurs @2pm
"""

def password_mod():
    word = input()
    password = ''
    x = len(word)
    while len(word) - x < len(word):
        if word[len(word)-x] == 'm':
            password = password + 'M'
        elif word[len(word)-x] == 'i':
           password = password + '1'
        elif word[len(word)-x] == 'a':
           password = password + '@'
        elif word[len(word)-x] == 'B':
           password = password + '8'
        elif word[len(word)-x] == 's':
           password = password + '$'
        else:
           password = password + word[len(word)-x]
        x= x - 1
    else: 
     password = password + '!'
     print(password)

if __name__ == "__main__":
    password_mod()