def CountNow(PLACES):
    for key in PLACES:
        if (len(PLACES[key]))>5:
            final=PLACES[key].upper()
            print(final)
PLACES={1:"Delhi", 2:"London", 3:"Paris", 4:"New York", 5:"Doha"}
CountNow(PLACES)    
