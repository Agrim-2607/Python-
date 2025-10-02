 a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
d=int(input("Enter the first number"))
if a>b:
   if a>c:
       if a>d:
           print("a is the greatest number")
       else:
           print("d is the greatest number")
   else:
       if c>d:
           print("c is the greatest number")
       else:
           print("d is the greatest number")
           
else:
    if b>c:
        if b>d:
           print("d is the greatest number")
        else:
           print("b is the greatest number")
    else:
        if c>d:
           print("c is the greatest number")
        else:
           print("d is the greatest number")
