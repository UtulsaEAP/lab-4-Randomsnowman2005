"""
Complete the following python code to reverse the string entered by the user.

Name: Mohamad ali Fakhoury
Lab Time: Thurs @2pm
"""

def reverse_string():
    x = 0
    inputs = []
    inp1 = ''
    z=0
    outputs = []
    while z<1 :
        inp1 = str(input())
        if inp1 =="done" or inp1 =="d" or inp1 == "Done":
         z = z+1
        else: 
         inputs.insert(x,inp1)
         x = x + 1
    else:  
        x=x-1
        z = 0
        while x >=0:
         z = len(inputs[x])
         final = ''
         while z> 0:
            word = inputs[x]
            let = word[z-1]
            final = final + let
            z = z -1
         outputs.insert(x,final)
         x=x-1
    x= len(outputs) - 1
    while x>=0:
     print (outputs[x])
     x= x - 1   

if __name__ == "__main__":
    reverse_string()