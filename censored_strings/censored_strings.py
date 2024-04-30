def uncensor(text:str, vowels:str) -> str:
    text:list = list(text)
    n:int = 0

    for i in range(len(text)):
        if text[i] == "*":
            text[i] = vowels[n]
            n += 1

    return "".join(text)


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))


'''
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
'''