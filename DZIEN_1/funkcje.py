print((lambda g:g**3)(87))

b = lambda a,b,c=1:(a+b)*c

print(b(9,4,2))
print(b(9,4))

def policz(n):
    return lambda a:a*n

print(policz(9)(3))

num = [67,3,-8,3,12,0,99,78,5,17,-99,4,18,8,-11]
