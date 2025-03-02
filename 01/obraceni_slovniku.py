# Napiš funkci, která ze slovníku vytvoří nový slovník, kde klíče a hodnoty budou zaměněné
# Použij dict comprehension


def obrat_slovnik(slovnik):
    naopak = {hodnota: klic for klic, hodnota in slovnik.items()}
    return naopak

