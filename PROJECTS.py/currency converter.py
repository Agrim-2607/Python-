
print('''
Conversions Available Between:
Indian Rupee - United States Dollar (INR-USD)
Indian Rupee - Australian Dollar (INR-ASD)
Indian Rupee - Canadian Dollar (INR-CAD)
Indian Rupee - Great British Pound (INR-GBP)
Indian Rupee - Euro (INR-EUR)
Indian Rupee - United Arab Emirates Dirham (INR-AED)
Indian Rupee - Swiss Franc (INR-CHF)
*(as of 20 November 2022)
===============================''')
    
b = ['Indian Rupee', 'INR']
c = ['United States Dollar', 'USD']
d = ['Australian Dollar', 'ASD']
e = ['Canadian Dollar', 'CAD']
f = ['Great British Pound', 'GBP']
g = ['Euro', 'EUR']
h = ['United Arab Emirates Dirham', 'AED']
i = ['Swiss Franc', 'CHF']
   
x = input("Convert from: ")
y = input("Convert to: ")
z = int(input("Enter Amount: "))
    
if x in b:
    if y in c:
        v = z * 0.012
    elif y in d:
        v = z * 0.018
    elif y in e:
        v = z * 0.016
    elif y in f:
        v = z * 0.010
    elif y in g:
        v = z * 0.012
    elif y in h:
        v = z * 0.045
    elif y in i:
        v = z * 0.012
    else:
        print("Conversions not available/Wrong input")
elif x in c and y in b:
    v = z * 81.52
elif x in d and y in b:
    v = z * 54.41
elif x in e and y in b:
    v = z * 60.77
elif x in f and y in b:
    v = z * 96.97
elif x in g and y in b:
    v = z * 84.34
elif x in h and y in b:
    v = z * 22.19
elif x in i and y in b:
    v = z * 85.43
else:
    print("Conversion not available/Wrong input")
print(z, x, '=', v, y)
