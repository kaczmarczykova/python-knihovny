# task_19_is_palindrome.py

def is_palindrome(s: str) -> bool:
    """
    Vrátí True, pokud je řetězec palindrom.
    """
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True
