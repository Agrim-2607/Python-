def calc_sum(n):
    if n==0:
        return 0
    
    return (calc_sum(n-1)+n)

n=int(input("Enter a number: "))
print(calc_sum(n))