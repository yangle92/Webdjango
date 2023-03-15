# 常见异常
# NameError
#print(1+'a')  #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(1+)  # SyntaxError: invalid syntax

d={'x':1}
#print(d['c'])  #KeyError: 'c'
l=[1,2]
#print(l[3])  #IndexError: list index out of range


# 异常万能捕获  Exception
try:
    d = {'x': 1}
    l=[1,2]
except NameError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print()


# 自定义异常
l=[1,2]
if len(l) != 2:
    raise TypeError('列表长度必须为5')
# 断言
l=[1,2]
assert  len(l) == 2


def d1(f):
    print('我是第一个装饰器')
    def inner():
        f()
    return inner


def d2(f):
    print('我是第二个装饰器')
    def inner():
        f()
    return inner

@d2
@d1
def f():
    print('我是主体函数，我需要装饰')

f()
