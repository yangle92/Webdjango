
a=3

def f1():
    global a
    a+=3
    print(a)

def f2():
    b=3
    def ineer():
        nonlocal b
        b+=3
        print(b)

    return ineer()
# f2()

a=[1,2,3,4]
b=[4,5,6,9]
c=zip(a,b)
d =[i for i in c]
# print(d)

def f3():
    print(f're fun')
    f3()

f3()
