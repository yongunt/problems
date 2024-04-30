num_holder:dict = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}


def letter_combinations(digits:str) -> list:
    output:list = [""]
    for d in digits:
        temp:list = []
        for v in num_holder[d]:
            for o in output:
                temp.append(o+v)
        output = temp
    return sorted(output)


print(letter_combinations("23"))
print(letter_combinations("532"))


'''
letter_combinations("23") ➞ ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

letter_combinations("532") ➞ ["jda", "jdb", "jdc", "jea", "jeb", "jec", "jfa", "jfb", "jfc", "kda", "kdb", "kdc", "kea", "keb", "kec", "kfa", "kfb", "kfc", "lda", "ldb", "ldc", "lea", "leb", "lec", "lfa", "lfb", "lfc"]
'''