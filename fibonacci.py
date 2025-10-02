n=int(input("Enter the no of iterations"))
a=0
b=1
print(a)
print(b)
for i in range(0,n):
    c=a+b
    print(c)
    a,b=b,c
    
