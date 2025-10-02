while True:
    string1=input("Enter the string:")
    print(string1)
    starting=string1[0:2]
    end=string1[len(string1):(len(string1)-3):-1]
    ending=end[::-1]
    new=starting+ending
    print(new)
    ch=input("do you want to inpur another string?Y/N")
    if ch=="N" or ch=="n":
        break
