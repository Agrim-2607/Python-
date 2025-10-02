a=int(input("enter 1 number:"))
b=int(input("enter 2 number:"))
c=int(input("enter 3 number:"))
d=int(input("enter 4 number:"))
if a>b and a>c and a>d:
    print("the greatest number is",a)
elif b>a and b>c and b>d:
    print("the greatest number is",b)
elif c>a and c>b and c>d:
    print("the greatest number is",c)
else:
    print("the greatest number is",d)    