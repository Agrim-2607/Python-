print('''
Conversions available between:
Kilometer-Meter (km-m)
Kilometer-Mile (km-mi)
Kilometer-Feet (km-ft)
Kilogram-Gram (kg-g)
Kilogram-Pound (kg-lb)
Kilogram-Tonne (kg-t)
Celsius-Fahrenheit (C-F)
Celsius-Kelvin (C-k)
===============================
''')
    
b = ['Kilometer', 'km']
c = ['Meter', 'm']
d = ['Mile', 'mi']
e = ['Feet', 'ft']
f = ['Kilogram', 'kg']
g = ['Gram', 'g']
h = ['Pound', 'lb']
i = ['Tonne', 't']
j = ['Celsius', 'C']
k = ['Fahrenheit', 'F']
l = ['Kelvin', 'k']
    
x = input("Convert from: ")
y = input("Convert to: ")
z = int(input("Enter Amount: "))
    
if x in b:
    if y in c:
        v = z * 1000
        print(z, x, '=', v, y)
    elif y in d:
        v = z * 0.621
        print(z, x, '=', v, y)
    elif y in e:
        v = z * 3280.84
        print(z, x, '=', v, y)
    else:
        print("Conversion not available/Wrong input")
elif x in c and y in b:
    v = z / 1000
    print(z, x, '=', v, y)
elif x in d and y in b:
    v = z * 1.609
    print(z, x, '=', v, y)
elif x in e and y in b:
    v = z * 0.0003048
    print(z, x, '=', v, y)
elif x in f:
    if y in g:
        v = z * 1000
        print(z, x, '=', v, y)
    elif y in h:
        v = z * 2.20462
        print(z, x, '=', v, y)
    elif y in i:
        v = z * 0.001
        print(z, x, '=', v, y)
    else:
        print("Conversion not available/Wrong input")
elif x in g and y in f:
    v = z * 0.001
    print(z, x, '=', v, y)
elif x in h and y in f:
    v = z * 0.4535
    print(z, x, '=', v, y)
elif x in i and y in f:
    v = z * 1000
    print(z, x, '=', v, y)
elif x in j:
    if y in k:
        v = z * 9 / 5 + 32
        print(z, x, '=', v, y)
    elif y in l:
        v = z + 273.15
        print(z, x, '=', v, y)
    else:
        print("Conversion not available/Wrong input")
elif x in k and y in j:
    v = (z - 32) * 5 / 9
    print(z, x, '=', v, y)
elif x in l and y in j:
    v = z - 273.15
    print(z, x, '=', v, y)
else:
    print("Conversion not available/Wrong input")
