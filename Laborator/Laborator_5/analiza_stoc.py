

pret = 23
cantitate = 50

valoare_totala = pret * cantitate

# definire functii
def calcul_valoare_totala_stoc(pret_unitar, stoc):
    rezultat = 0
    rezultat = pret_unitar * stoc
    return rezultat

valoare_totala = calcul_valoare_totala_stoc(pret, cantitate)

print("Valoare totala stoc: ", valoare_totala)

# liste/vectori
valori = []
valori_cunoscute = [10,20,30,40,50]
print("Prima valoare este : ", valori_cunoscute[0])
valori.append(10)
valori.append(20)
valori_cunoscute.append(60)
valori_cunoscute.insert(2, 1)

# prelucrare lista
# varianta Python
total = 0
for valoare in valori_cunoscute:
    total = total + valoare

print("Total: ", total)

# varianta similara C cu index
total = 0
for index in range(0, len(valori_cunoscute)):
    total = total + valori_cunoscute[index]

print("Total: ", total)

print(valori)
print(valori_cunoscute)

#definire metoda/functie care citeste un int cu validari
def citireInt(mesaj_input, mesaj_eroare, valoare_minima):
    valoare_input = 0
    valoare_corecta = False
    while valoare_corecta == False:
        valoare_corecta = True
        valoare_input = int(input(mesaj_input))
        if valoare_input >= valoare_minima:
            break
        else:
            valoare_corecta = False
            print(mesaj_eroare)
    return valoare_input

pret = citireInt("Pretul unitar (minim 1):", "Pretul este incorect", 1)
stoc = citireInt("Stocul (minim 0):", "Stocul este incorect", 0)

print("Pret citit: ", pret)


