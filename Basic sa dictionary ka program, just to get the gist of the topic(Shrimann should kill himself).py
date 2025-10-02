def dictionary():
    d={1:'a',2:'B',3:'c'}
    print(len(d))
    print(d.get(1))
    print(d.keys())
    print(d.values())
    d2=dict.fromkeys([1,2,3,4,5],5)
    print(d2)
    d.setdefault(1,'A')
    print(d)
    d3={1:'A',2:'B',3:'c'}
    d.update(d3)# whatever in d3 will be copied in d
    print(d)
    print(d3)
    #same
    d3=d2.copy()
    d4={}
    print("copy",d3)
    print(d3.pop(5))
    print(d.popitem())
    d4.clear()
    print(d4)
    sorted(d)
    print(d)
    print(max(d))
    print(min(d))
    print(sum(d))
dictionary()
