from string import ascii_lowercase as ALP 


def alphabet_index(word:str) -> str:
    highest_ind:int = 0
    current_letter:str = ""

    for i in word.lower():
        if (ALP.index(i) + 1) > highest_ind:
            highest_ind = ALP.index(i) + 1
            current_letter = i

    return str(highest_ind) + current_letter


print(alphabet_index("Flavio"))
print(alphabet_index("Andrey"))
print(alphabet_index("Oscar"))


'''
alphabet_index(alphabet, "Flavio") ➞ "22v"

alphabet_index(alphabet, "Andrey") ➞ "25y"

alphabet_index(alphabet, "Oscar") ➞ "19s"
'''