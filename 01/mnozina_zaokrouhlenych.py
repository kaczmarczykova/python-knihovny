# Napiš funkci, která vrátí ze iterovatelného vstupu množinu zaokrouhlených hodnot

def mnozina_zaokrouhlenych(vstup):
    mnozina = {round(cislo) for cislo in vstup}
    return mnozina
