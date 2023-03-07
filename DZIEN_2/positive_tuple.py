class PositiveTuple(tuple):
    def __new__(cls, *numbers):
        skipped_value = 0
        positive_numbers = []
        for x in numbers:
            if x>=0:
                positive_numbers.append(x)
            else:
                skipped_value += 1

        instance = super().__new__(cls,tuple(positive_numbers))
        instance.skipped_value = skipped_value
        return instance

pnb = PositiveTuple(90,0,7,8,-1,-77,0,45,6,7,-23,-3)
print(pnb)
print(type(pnb))
print(pnb.skipped_value)
