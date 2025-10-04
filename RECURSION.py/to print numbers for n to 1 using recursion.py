def p(n):
    if n==0:
        return
    print(n)
    p(n-1)
n=int(input("Enter a number: "))
p(n)