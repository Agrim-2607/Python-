#Method2
string=input("Enter the string:")
reverse=string[::-1]
if string==reverse:
    print("String is palindrome...")
else:
    print("String is not palindrome..")

#Method2
'''
string=input("Enter the string:")
l=len(str(string))
reverse=''
for i in range(l-1,-1,-1):
    reverse+=string[i]
if string==reverse:
    print("String is palindrome...")
else:
    print("String is not palindrome..")
'''
