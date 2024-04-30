from string import ascii_lowercase

def condi_cipher(message, key, shift):
    new_key = []
    ans = ""

    for i in key:
        if i not in new_key: new_key.append(i)

    alp = [i for i in ascii_lowercase if i not in new_key]

    alp = new_key + alp

    for i in message:
        if i in alp:
            ans += alp[(alp.index(i) + shift) % 26]
            shift = alp.index(i) + 1
        else: ans += i

    return ans


print(condi_cipher("on.,", "cryptogam", 10))
print(condi_cipher("mubashir", "airforce", 6))
print(condi_cipher("matt", "edabit", 2))


'''
condi_cipher("on.,", "cryptogam", 10) ➞ "jx.,"

condi_cipher("mubashir", "airforce", 6) ➞ "ugrdtfko"

condi_cipher("matt", "edabit", 2) ➞ "opgk"
'''