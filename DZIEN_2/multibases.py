class MultiBases(type):
    def __new__(cls, clsname, bases, clsdict):
        if len(bases) > 1:
            raise TypeError("Dostępne jest jedynie jednodziedziczenie")
        return super().__new__(cls, clsname, bases, clsdict)


class Base(metaclass=MultiBases):
    pass

class Reg():pass

class B(Base):pass

class C(B,Reg):pass
