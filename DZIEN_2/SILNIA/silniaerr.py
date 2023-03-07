class SilniaErr(Exception):
    def __init__(self,n):
        self.n=n
    def __str__(self):
        return f"wartość n={self.n} jest niewłaściwa! Silnia jest zdefinowana tylko dla liczb > 0"
