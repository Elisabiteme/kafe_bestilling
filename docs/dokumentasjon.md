# Dokumentasjon: Kafé-bestillingssystem

## Oversikt
Dette prosjektet er et enkelt objektorientert Python-program som simulerer et bestillingssystem for en kafé. Programmet lar deg opprette produkter, kunder og bestillinger, samt vise kvittering med totalpris og eventuelle rabatter.

## Filstruktur
Kun én Python-fil kreves: `kafe_bestilling.py`

## Klasser

### `Produkt`
Representerer et produkt i kaféens meny.
- **Attributter:**
  - `navn` (str): Navn på produktet
  - `pris` (float): Pris i kroner

### `Bestillingslinje`
Representerer en linje i en bestilling (et produkt og antall).
- **Attributter:**
  - `produkt` (Produkt): Produktet som bestilles
  - `antall` (int): Hvor mange enheter som bestilles
- **Metoder:**
  - `totalpris()`: Returnerer totalprisen for linjen

### `Kunde`
Representerer en kunde som gjør en bestilling.
- **Attributter:**
  - `navn` (str)
  - `telefon` (str)

### `Bestilling`
Representerer en hel bestilling med en eller flere bestillingslinjer.
- **Attributter:**
  - `kunde` (Kunde): Kunden som har bestilt
  - `dato` (date): Dato for bestillingen
  - `linjer` (liste av Bestillingslinje)
  - `rabatt` (int): Rabatt i prosent (valgfritt)
  - `ordre_id` (int): Automatisk generert ordre-ID
- **Metoder:**
  - `legg_til(produkt, antall)`: Legger til en ny linje
  - `total()`: Regner ut totalpris, med rabatt hvis oppgitt
  - `vis_kvittering()`: Skriver ut kvittering til terminalen

## Bruk
Eksempelet nederst i filen viser hvordan man:
1. Lager produkter
2. Lager en kunde
3. Lager en bestilling
4. Legger produkter til bestillingen
5. Viser kvittering

## Eksempel på kjøreresultat
```
Ordre-ID: 1
Bestilling for Elisabet Witsø (12345678) - 2025-04-22
2 x Kaffe = 70 kr
1 x Kake = 50 kr
1 x Te = 30 kr
Rabatt: 10%
Totalt: 135.0 kr
```

## Mulige utvidelser
- Input fra bruker (CLI-meny)
- Skrive kvittering til fil
- Statistikk over mest solgte produkter
- Lagerbeholdning
- GUI med tkinter eller webgrensesnitt

## Lisens
Prosjektet kan lisensieres med MIT-lisens, GPL eller etter ønske.

## For GitHub
Legg inn:
- `README.md` med denne dokumentasjonen
- Kildekode i `kafe_bestilling.py`
- Eventuelt `.gitignore` og lisensfil

Ta gjerne kontakt hvis du vil jeg skal generere README automatisk.

