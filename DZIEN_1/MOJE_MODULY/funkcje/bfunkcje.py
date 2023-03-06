def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f"element listy ne {i+1} -> {j}")

def czytaj_dict(dictionary):
    for x,y in dictionary.items():
        print(f"klucz -> {x}: wartośc: {y}")
