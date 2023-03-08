import asyncio
import random

#ANSI colors
c = (
    "\033[0m", #koniec kolorowania
    "\033[36m", #Cyan
    "\033[91m", #Czerwony
    "\033[35m" #Magenta
)

async def makerandom(idx:int,threshold:int=6)->int:
    print(c[idx+1]+f"inicjacja makerandom({idx}).")
    i = random.randint(0,10)
    while i <= threshold:
        print(c[idx+1] + f"makerandom({idx}) == {i} zbyt małe, powtórz losowanie...")
        await asyncio.sleep(idx+1)
        i = random.randint(0,10)
    print(c[idx+1] + f"--->Zakończono: makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    res = await asyncio.gather(*(makerandom(i,10-i-1) for i in range(3)))
    return res

if __name__ == '__main__':
    random.seed(444)
    r1,r2,r3 = asyncio.run(main())
    print("______________________________________")
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
