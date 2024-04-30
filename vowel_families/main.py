def same_vowel_group(words:list[str]) -> list[str]:
    VOWELS:str = "aeiou"
    vowel_holder:list[str] = [letter for letter in words[0] if letter in VOWELS]
    temp:list[str] = []
    ans:list[str] = []
    flag:bool = True

    for word in words:
        temp = [letter for letter in word if letter in VOWELS]
        for letter in temp:
            if letter not in vowel_holder:
                flag = False
                break
        if flag: ans.append(word)
        flag = True

    return ans


print(same_vowel_group(["toe", "ocelot", "maniac"]))
print(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]))
print(same_vowel_group(["hoops", "chuff", "bot", "bottom"]))


'''
same_vowel_group(["toe", "ocelot", "maniac"]) ➞ ["toe", "ocelot"]

same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) ➞ ["many"]

same_vowel_group(["hoops", "chuff", "bot", "bottom"]) ➞ ["hoops", "bot", "bottom"]
'''