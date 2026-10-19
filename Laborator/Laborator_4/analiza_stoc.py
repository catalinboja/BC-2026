# etape
# 1. citire date input
# 2. validare input - sa nu fie negativ
# 3. analiza stoc final
# 4. simulare livrari

# definire variabile


denumire_produs = ""
stoc_initial = 0
cantitate_receptionata = 0
stoc_minim = 0
dateinput_valide = False


denumire_produs = input("Denumire produs: ")

while dateinput_valide == False:

    dateinput_valide = True

    stoc_initial = int(input("Stoc initial: "))

    if stoc_initial < 0:
        print("Stoc negativ !")
        dateinput_valide = False

    cantitate_receptionata = int(input("Cantitate primita: "))

    if cantitate_receptionata < 0:
        print("Cantitate receptionata negativa")
        dateinput_valide = False

    stoc_minim = int(input("Stoc minim: "))

    if stoc_minim < 0:
        print("Stoc minim negativ")
        dateinput_valide = False


print(denumire_produs, stoc_initial, cantitate_receptionata, stoc_minim, dateinput_valide)

# analiza financiara
stoc_final = stoc_initial + cantitate_receptionata
print(f"Stoc final {stoc_final}")

if stoc_final == 0:
    print("Stoc epuizat")
elif stoc_final < stoc_minim:
    print("Reaprovizionare necesara")
else:
    print("Stoc suficient")


for iteratie in range(1, 4):
    print("Receptie ", iteratie, ": ")
    #print(f"Receptie {iteratie}:")
    cantitate_noua = int(input("Cantitate: "))
    stoc_final = stoc_final + cantitate_noua

print("Stoc total", stoc_final)
