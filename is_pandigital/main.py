def is_pandigital(n:int) -> bool:
    n:list = list(str(n))
    if '0' in n: return False
    digits:list = [str(i) for i in range(1, len(n)+1)]

    for i in range(len(digits)):
        try: n.pop(n.index(digits[i]))
        except: return False

    if n != []: return False
    return True


print(is_pandigital("12"))
print(is_pandigital("18734256"))
print(is_pandigital("1231263876"))
print(is_pandigital("192783654"))