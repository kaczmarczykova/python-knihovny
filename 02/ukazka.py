import sys

minut_celkem = int(sys.argv[1])
hodiny = minut_celkem // 60
minuty = minut_celkem % 60
print(f'{hodiny}:{minuty}')