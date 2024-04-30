vowels:str = "aeiou"

def vowel_links(sentence:str) -> bool:
    for i in range(2, len(sentence)):
        if sentence[i].lower() in vowels and sentence[i-1] == ' ' and sentence[i-2].lower() in vowels: return True

    return False


print(vowel_links("a very large appliance"))
print(vowel_links("go to edabit"))
print(vowel_links("an open fire"))
print(vowel_links("a sudden applause"))


'''
vowel_links("a very large appliance") ➞ True

vowel_links("go to edabit") ➞ True

vowel_links("an open fire") ➞ False

vowel_links("a sudden applause") ➞ False
'''