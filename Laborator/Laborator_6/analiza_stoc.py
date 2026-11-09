
# definire variabile cunoscute
denumire = ""
pret_unitar = 0
cost_achizitie = 0
cantitati_vandute = [15,10,3,21,7] #in ultimele 5 zile

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

def citireFloat(mesaj_input, mesaj_eroare, valoare_minima):
    valoare_input = 0
    valoare_corecta = False
    while valoare_corecta == False:
        valoare_corecta = True
        valoare_input = float(input(mesaj_input))
        if valoare_input >= valoare_minima:
            break
        else:
            valoare_corecta = False
            print(mesaj_eroare)
    return valoare_input

def get_total_cantitati_vandute(valori):
    if len(valori) == 0:
        return 0
    total = 0
    for valoare in valori:
        total += valoare
    return total

def get_total_cantitati_vandute_2(valori):
    return sum(valori)

def get_venit_total(pret_unitar, cantitate_vanduta):
    return pret_unitar * cantitate_vanduta

def get_cost_total(cost_achizitie, cantitate_vanduta):
    return cost_achizitie * cantitate_vanduta

def get_profit(venit, costuri):
    return venit - costuri

def get_medie_vanzari(vanzari_zilnice):
    if(len(vanzari_zilnice) == 0):
        return 0
    total = sum(vanzari_zilnice)
    return total / len(vanzari_zilnice)

def get_numar_zile_peste_medie(vanzari_zilnice, medie_vanzari):
    numar_zile = 0
    #varianta 1
    # for valoare in vanzari_zilnice:
    #     if valoare >= medie_vanzari:
    #         numar_zile +=1 
    # return numar_zile

    #varianta 2
    for i in range(len(vanzari_zilnice)):
        if vanzari_zilnice[i] >= medie_vanzari:
            numar_zile += 1
    return numar_zile

def analiza_profi(profit_total):
    if profit_total > 0:
        print("Activitate profitabilă")
    elif profit_total == 0:
        print("Prag de rentabilitate")
    else:
        print("Activitate neprofitabilă")


pret_unitar = citireInt("Pretul unitar (minim 1):", "Pretul este incorect", 1)
cost_achizitie = citireFloat("Costul de achizitie (minim 0):", "Costul este incorect", 0)
denumire = input("Denumire produs: ")

print("Pret unitar: ", pret_unitar)
print("Cost achizitie: ", cost_achizitie)
print("Denumire: ", denumire)
print("Vanzari: ", cantitati_vandute)

#testare functii
print("Total vanzari: ", get_total_cantitati_vandute(cantitati_vandute))
print("Total vanzari: ", get_total_cantitati_vandute_2(cantitati_vandute))

total_cantitate_vanduta = get_total_cantitati_vandute_2(cantitati_vandute)
venit_total = get_venit_total(pret_unitar, total_cantitate_vanduta)
print("Venit total: ", venit_total)
print("Cost total: ", get_cost_total(cost_achizitie, total_cantitate_vanduta))
print("Profit: ", get_profit(venit_total, get_cost_total(cost_achizitie, total_cantitate_vanduta)))

medie_vanzari = get_medie_vanzari(cantitati_vandute)
print("Medie vanzari: ", medie_vanzari)
print("Nr zile peste medie: ", get_numar_zile_peste_medie(cantitati_vandute, medie_vanzari))
