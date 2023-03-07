class MyError(Exception):
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("wywołanie konstuktora __str__")
        if self.message:
            return f"{self.__class__.__name__} -> {self.message}"
        else:
            return f"{self.__class__.__name__} "

try:
    n = 100
    if n == 100:
        raise MyError('n nie może wynosić 100')
except MyError as m:
    print(m)
