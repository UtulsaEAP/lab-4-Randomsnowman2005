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
    x = -10
    y = -10
    for  x in range(-10,10):
      for y in range(-10,10):
         if (x*a)+(x*b)==c and (x*d)+(x*e)==f:
            print(f'x = {x} , y = {y}')
            break
         elif y<=10:
            y =y+1
         else: x=x+1
    else: print('There is no solution ')
    print(x,y)
    

    
    
if __name__ == "__main__":
    brute_eq()