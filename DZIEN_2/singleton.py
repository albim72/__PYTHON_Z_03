class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Regular():
    pass

r1 = Regular()
r2 = Regular()

print(r1 == r2)
print(r1)
print(r2)

class SngClass(metaclass=Singleton):
    pass

s1 = SngClass()
s2 = SngClass()

print(s1 == s2)
print(s1)
print(s2)
