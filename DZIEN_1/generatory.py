#przykład 1
def liczby():
    for i in range(16):
        yield i*2

print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)


#przykład 2
def wznowienie(n,k):
    print("wstrzymanie działania")
    yield 1001
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n+k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n-k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n*k
    print("wznowienie działania")

for i in wznowienie(8,5):
    if i==1001:
        continue
    print(f"wartość z yield: {i}")
