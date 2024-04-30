def remove_letters(letters:list, word:str) -> list:
    holder:list = []
    word:list = list(word)

    for letter in letters:
        if letter in word:
            x:int = word.count(letter)
            for i in range(x):
                word.remove(letter)
                holder.append(letter)

    for i in holder:
        if i in letters: letters.remove(i)

    return letters


print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))


'''
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []
'''