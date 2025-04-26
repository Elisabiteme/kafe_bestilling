
#BESTILLINGSSYSTEM FOR EN KAFE: 
#lar deg lage bestillinger, legge til produkter (som kaffe, kake, te), legge inn rabatt og regne ut og og vise kvittering.

from datetime import date

class Produkt:
    def __init__(self, navn, pris):
        self.navn = navn
        self.pris = pris

class Bestillingslinje:
    def __init__(self, produkt, antall):
        self.produkt = produkt
        self.antall = antall

    def totalpris(self):
        return self.antall * self.produkt.pris

class Kunde:
    def __init__(self, navn, telefon):
        self.navn = navn
        self.telefon = telefon

class Bestilling:
    teller = 1

    def __init__(self, kunde, rabatt=0):
        self.kunde = kunde
        self.dato = date.today()
        self.linjer = []
        self.rabatt = rabatt
        self.ordre_id = Bestilling.teller
        Bestilling.teller += 1

    def legg_til(self, produkt, antall):
        self.linjer.append(Bestillingslinje(produkt, antall))

    def total(self):
        total = sum(linje.totalpris() for linje in self.linjer)
        if self.rabatt > 0:
            total *= (1 - self.rabatt / 100)
        return round(total, 2)

    def vis_kvittering(self):
        print(f"\nOrdre-ID: {self.ordre_id}")
        print(f"Bestilling for {self.kunde.navn} ({self.kunde.telefon}) - {self.dato}")
        for linje in self.linjer:
            print(f"{linje.antall} x {linje.produkt.navn} = {linje.totalpris()} kr")
        if self.rabatt > 0:
            print(f"Rabatt: {self.rabatt}%")
        print(f"Totalt: {self.total()} kr\n")

# Eksempelbruk
if __name__ == "__main__":
    kaffe = Produkt("Kaffe", 35)
    kake = Produkt("Kake", 50)
    te = Produkt("Te", 30)

    kunde1 = Kunde("Elisabet", "12345678")

    bestilling1 = Bestilling(kunde1, rabatt=10)
    bestilling1.legg_til(kaffe, 2)
    bestilling1.legg_til(kake, 1)
    bestilling1.legg_til(te, 1)

    bestilling1.vis_kvittering()
