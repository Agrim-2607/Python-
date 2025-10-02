a=int(input("enter 1 number:"))
b=int(input("enter 2 number:"))
c=int(input("enter 3 number"))
if a>b and a>c:
    print("the largest number",a)
elif b>a and b>c:
    print("the largest number",b)
else:
    print("the largest number",c)
# if a>b:
#     if a>c:
#         print("print a is the greatest number", a)
#     else:
#         print("print c is the greatest number", c)
# elif b>a:
#     if b>c:
#         print("print b is the greatest number", b)
#     else:
#         print("print c is the greatest number", c)