from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Pełna nazwa metody: {func.__qualname__}")
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls

@debugmethods
class Calc:
    def add(self,x,y):
        return x+y

    def mul(self,x,y):
        return x*y

    def div(self,x,y):
        return x/y

mycalc = Calc()
print(mycalc.add(4,6))
print(mycalc.mul(4,6))
