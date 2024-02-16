"""
Complete the following python code to take in a list of values from the user and then normalize them

Name:Mohamad Ali Fakhoury
Lab Time: Thurs @ 2pm
"""

def norm():
    nran = int(input())
    i = 0
    ran =[]
    while i < nran:
        ran.insert(i,float(input()))
        i = i + 1
    i=0
    for i in range(0, nran-1):
        if ran[i] > ran[i+1]:
            div = ran[i]
        if ran[nran-1] > ran[i]:
            div = ran[nran-1]
    for i in range(0, nran):   
        print(f'{ran[i]/div:.2f}') 

    
if __name__ == "__main__":
    norm()