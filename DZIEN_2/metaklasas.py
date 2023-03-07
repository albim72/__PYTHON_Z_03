class MojaMeta(type):
    def __new__(cls,clsname,bases,attribs):
        print(f"nazwa klasy: {clsname}")
        print(f"dziedziczone klasy: {bases}")
        print(f"zbiór atrybutów: {attribs}")
        return type.__new__(cls,clsname,bases,attribs)


class Regular():
    pass

class Base(Regular,metaclass=MojaMeta):
    pass

class Next(Base):
    pass

class Second:
    pass

class Last(Second,Next):
    pass
