# task_30_remove_duplicates.py

def remove_duplicates(nums: list[int]) -> list[int]:
    """
    Odstraní duplikáty ze seznamu a zachová pořadí.
    """

    seen = set()  # Množina pro sledování již viděných prvků
    result = []  # Výsledek bez duplikátů

    for num in nums:
        if num not in seen:  # Pokud prvek ještě nebyl přidán
            seen.add(num)  # Přidáme ho do množiny
            result.append(num)  # A do výsledného seznamu

    return result
