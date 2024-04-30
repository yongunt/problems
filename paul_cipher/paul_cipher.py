from string import ascii_uppercase as ALP

def paul_cipher(message):
    message = message.upper()
    ans = ""
    holder = ""

    for i in message:
        if i in ALP:
            ans += i
            holder += i
            DETERMINE = message.index(i) + 1 
            break
        else: ans += i

    for i in message[DETERMINE::]:
        if i in ALP:
            current = ALP.index(holder[-1])
            ans += ALP[(ALP.index(i) + current + 1) % len(ALP)]
            holder += i 
        else: ans += i
    
    return ans


print(paul_cipher("he1lo"))
print(paul_cipher("muBas41r"))
print(paul_cipher("a1rForce"))
print(paul_cipher("MATT"))


'''
paul_cipher("he1lo") ➞ "HM1QA"

paul_cipher("muBas41r") ➞ "MHWCT41K"

paul_cipher("a1rForce") ➞ "A1SXUGUH"

paul_cipher("MATT") ➞ "MNUN"
'''