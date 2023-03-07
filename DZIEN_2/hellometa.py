class HelloMeta(type):
    def hello(cls):
        print(f"klasa typu: {type(cls())}")

    def __call__(self, *args, **kwargs):
        cls = type.__call__(self,*args)
        setattr(cls,"hello",self.hello)
        return cls

class TryHello(object, metaclass=HelloMeta):
    def greet(self):
        self.hello()

gt = TryHello()
gt.greet()
