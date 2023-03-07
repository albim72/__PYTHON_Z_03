import types

def notify(fn,*args,**kwargs):
    def fncomposite(*args,**kwargs):
        print(f"running: {fn.__name__}")
        rt = fn(*args,**kwargs)
        return rt
    return fncomposite


class Notifies(type):
    def __new__(cls,name, bases, attrs):
        for name, value in attrs.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attrs[name] = notify(value)
        return super(Notifies,cls).__new__(cls,name, bases, attrs)


class Math(metaclass=Notifies):
    def multiply(a,b):
        prod= a*b
        print("mnożenie")
        return prod

print(Math.multiply(6,3))

class Tekstowa(metaclass=Notifies):
    def intro(self):
        print("inicjacja OK")

s = Tekstowa()
s.intro()
