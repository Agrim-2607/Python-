n=int(input("Enter the number to be checked:"))
s=0
order=len(str(n))
n1=n
while (n>0):
    digit=n%10
    s+=digit**order
    n=n//10

#a=n1//100
#n1=n1%100
#b=n1//10
#n1=n1%10
#s=(a*a*a)+(b*b*b)+(n1*n1*n1)

if s==n1:
    print("Asmstrong")
else:
    print("Not Armstrong")
