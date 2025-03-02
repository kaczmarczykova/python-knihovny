from random import randint
import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} <pocet_stran> <pocet_hodu>")

pocet_stran = int(sys.argv[1])
pocet_hodu = int(sys.argv[2])

print([randint(1, pocet_stran) for _ in range(pocet_hodu)])