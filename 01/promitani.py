# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani
nazvy = [
    'Někdo to rád horké, extended edition',
    'Adéla ještě nevečeřela',
    'Kulový blesk'
    ]
delky = [136, 105, 62]


def prevod(vstup):
    trvani = [(f"{cas // 60}:{(cas % 60):02d}") for cas in vstup]
    return trvani

prevod(delky)
