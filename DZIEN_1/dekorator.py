import time


#przykład 1
def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu.....")
        funkcja(*args)
        print("kończenie proces.....")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka")

zw = startstop(zawijanie)

zw("czekoladek")

print("____________________________________")
zawijanie("ciastek")
print("____________________________________")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} w urodziny")


dmuchanie("świeczek na torcie")
