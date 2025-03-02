from random import randint
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} <pocet_stran>")

print(randint(1, int(sys.argv[1])))