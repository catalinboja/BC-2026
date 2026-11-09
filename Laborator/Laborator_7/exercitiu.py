
# functie care citeste o lista de la terminal
def get_lista_terminal():
    numar_elemente = int(input("Numar elemente"))
    lista = []
    for index in range(numar_elemente):
        print("Element ", index + 1)
        valoare = int(input())
        lista.append(valoare)
    return lista

# filtrare lista produse dupa criteriu: contine o litera data
def get_filtrare_lista(filtru_denumire, lista):
    filtru = []
    for valoare in lista:
        if filtru_denumire in valoare:
            filtru.append(valoare)
    return filtru


def get_min_max(valori):
    if len(valori) == 0:
        return (0,0)
    min = valori[0]
    max = valori[0]
    for valoare in valori:
        if min > valoare:
            min = valoare
        if max < valoare:
            max = valoare
    return (min, max)


def get_min_max_2(valori):
    if len(valori) == 0:
        return (0,0)
    valoare_minima = min(valori)
    valoare_maximna = max(valori)
    return (valoare_minima, valoare_maximna)
    

# valori = get_lista_terminal()
# print(valori)

produse = ["LAPTOP ", "   Laptop", " laptop", "  tastatura", "MONITOR"]
if "LAPTOP" in produse:
    print("Avem laptop in lista")
else:
    print("Nu exista")

#normalizare - reducem valorile la UPPERCASE sau lowercase
# for denumire in produse:
#     denumire = denumire.lower()

for index in range(len(produse)):
    # lower case
    produse[index] = produse[index].lower()
    # eliminare spatii
    produse[index] = produse[index].strip()

print(produse)

produse_filtrate = get_filtrare_lista("apt", produse)
print(produse_filtrate)


exemplu_lista = [1,1,1,1,2,3,4]
exemplu_lista.append(4)
print(exemplu_lista)

exemplu_tuplu = (1,2,3,4)
exemplu_tuplu_valori_diferite = (1, "Laptop", 1100.45)
print(exemplu_tuplu)
print(exemplu_tuplu_valori_diferite)
print("Denumire: ", exemplu_tuplu_valori_diferite[1])
print("Id: ", exemplu_tuplu_valori_diferite[0])
print("Pret: ", exemplu_tuplu_valori_diferite[2])

print(get_min_max(exemplu_lista))
print(get_min_max_2(exemplu_lista))

exemplu_dictionar = {
    11: ("Laptop", 2500.0, 20),     #denumire, pret, stoc
    15: ("Smartphone", 3400.0, 15),
    23: ("Monitor", 780.0, 20)
}
print(exemplu_dictionar)
print(exemplu_dictionar.get(15))
exemplu_dictionar[25] = ("Test", 20, 1)
exemplu_dictionar[11] = ("Test", 20, 1)
#update
print(exemplu_dictionar)

exemplu_dictionar_2 = {
    11: ["Laptop", 2500.0, 20],     #denumire, pret, stoc
    15: ["Smartphone", 3400.0, 15],
    23: ["Monitor", 780.0, 20]
}
print(exemplu_dictionar_2)
exemplu_dictionar_2[11][0] = "Super laptop"
print(exemplu_dictionar_2)

dictionar_note = {
    "g1036": [9,9,10,7,8],  
    "g1035": [8,7,9,10,7,10]
}
print(dictionar_note["g1036"])

dictionar_studenti = {
    "g1036": {
        "Alice": (1,22, [9,10,10,10]), # id, varsta si note
        "John": (2,21, [7,8, 9])
    },
    "g1035": {
            "Bob": (1,22, [9,10,9,8]), # id, varsta si note
            "Test": (2,21, [7,8, 9])
        }
}

print(dictionar_studenti.get("g1036").get("Alice")[2])
print(dictionar_studenti["g1036"]["Alice"][2])