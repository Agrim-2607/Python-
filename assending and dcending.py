a=list(input("enter the no. of elements"))
f=int(input("FOR ASCENDING PRESS 0 AND FOR DESCENDING PRESS 1"))      
if f==0:
    a.sort()
    print(a)
elif f==1:
    a.sort()
    c=a[::-1]
    print(c)
