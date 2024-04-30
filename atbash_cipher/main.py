from string import ascii_lowercase as ALP
REVERSED_ALP:str = ALP[::-1] 


def atbash(seq:str) -> str:
    ans:str = ""

    for i in range(len(seq)):
        if seq[i].lower() in ALP: 
            if seq[i].isupper(): ans += REVERSED_ALP[ALP.index(seq[i].lower())].upper()
            else: ans += REVERSED_ALP[ALP.index(seq[i].lower())]
        else: ans += seq[i]

    return ans


print(atbash("apple"))
print(atbash("Hello world!"))
print(atbash("Christmas is the 25th of December"))


'''
atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
'''