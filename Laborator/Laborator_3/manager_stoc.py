#input
denumire_produs = ""
pret_unitar = 0.0
stoc_existent = 0
cantitate_livrata = 0

#output
cantitate_totala = 0
valoare_stoc_existent = 0.0
valoare_livrare = 0.0
valoare_totala_stoc = 0.0

denumire_produs = input("Denumire produs: ")
pret_unitar = float(input("Pret unitar: "))
stoc_existent = int(input("Stoc existent: "))
cantitate_livrata = int(input("Cantitate livrata: "))

#validare date input
#verificare pret > 0 si <= 1000
if pret_unitar > 0 and pret_unitar <= 1000:
    #calcule
    cantitate_totala = stoc_existent + cantitate_livrata
    #si restul
else:
    print("Pretul introdus este gresit !")

if pret_unitar <= 0 or pret_unitar > 1000:
    print("Pretul introdus este gresit !")
else :
    #calcul rezultate
    cantitate_totala = stoc_existent + cantitate_livrata
    valoare_stoc_existent = pret_unitar * stoc_existent
    valoare_livrare = pret_unitar * cantitate_livrata
    valoare_totala_stoc = valoare_stoc_existent + valoare_livrare

    print(f"Cantitate totala: {cantitate_totala}")
    print(f"Valoare stoc: {valoare_stoc_existent}")
    print(f"Valoare livrare: {valoare_livrare}")
    print(f"Valoare totala: {valoare_totala_stoc}")

for index_ziua in range (1,7):
    cantitate_zilnica = int(input(f"Cantitate primita in ziua {index_ziua}:"))
    cantitate_totala = cantitate_totala + cantitate_zilnica

print(f"Cantitate totala {cantitate_totala}")