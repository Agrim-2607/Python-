s=str(input("Enter the string"))
a=s.lower()
v=0
c=0
n=len(s)
v=a.count('a')+a.count('e')+a.count('i')+a.count('o')+a.count('u')
print(v)
c=n-v
print(c)
