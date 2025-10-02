l=[]
def SUM3(L):
    for i in range(len(L)):
        if L[i]%10==3:
            l.append(L[i])
            print(L[i])
L=[123,10,13,15,23]
SUM3(L)    
print("Sum of integers ending with 3:", sum(l))
