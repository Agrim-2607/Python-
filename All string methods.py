'''
a="agrim anshika"
print(a.upper())  #capitalize all the characters
print(a.isupper())  #state true or false whether the first letter is capital or not
print(a.lower()) #make all letters small
print(a.capitalize())  #capitalize first letter
print(a.title())  #it capitalize first letter of every word in a string
print(a.rstrip("im")) #remove letters from right side
print(a.lstrip("ag"))   #remove letters from left side
print(a.endswith("m"))  #state true or false whether the letter end with the given letter
print(a.startswith("a"))  #state true or false whether the letter start with the given letter
print(a.endswith("im"))
print(a.replace("agrim","anshika"))  #replaces the word with another word
print(a.find("a"))  #find the index of any character given as input 
b="he is my man"
#print(b.split(" "))  #it can convert into list
print(b.endswith("y",2,8))  #it also count the index of space
print(b.find("is"))   #it give the input in the form of index
print(len(b))
#print(index("is"))
print(b.isprintable())  #it gives false statement when there will be slash, it onluy give true statement when there will be proper characters
c=" "
print(c.isspace())  #it gives true output when the string is empty
print(b.swapcase()) #it converts all the letters into capital if it is small and vice versa
'''
help(len)
help(str)

