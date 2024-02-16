"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Mohamad Ali Fakhoury
Lab Time: Thurs @2pm
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())
    for  x in range(-10,10):
     for y in range(-10,10):
        g = a*x + b*y
        h = d*x + e*y
        if c==g and h==f:
           print(f'x = {x} , y = {y}')
           break
    if c!=g or h!=f:
     print("There is no solution")

    

    
    
if __name__ == "__main__":
    brute_eq()