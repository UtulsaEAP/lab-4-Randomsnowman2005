"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name:Mohamad ali Fakhoury
Lab Time: Thurs @2pm
"""

def inc_5():
    in1 = int(input())
    in2 = int(input())
    ad = 1
    sti = f'{in1}'
    if in1 <= in2:
        fin = in1 
        while fin < in2:
            fin = in1 + (5*ad)
            sti = sti + f' {str(fin)}'
            ad = ad+1
        else: print(sti)

    else: print("Second integer can't be less than the first.") 



if __name__ == '__main__':
    inc_5()