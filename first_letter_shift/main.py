def shift_sentence(sentence:str) -> str:
    sentence:list = [list(i) for i in sentence.split(' ')]
    first_letters:list = [i[0] for i in sentence]

    first_letters.insert(0, first_letters[-1])
    first_letters.pop(-1)
    
    for i in range(len(sentence)): sentence[i][0] = first_letters[i]
    
    sentence:list = [''.join(i) for i in sentence]

    return ' '.join(sentence)


print(shift_sentence("create a function"))
print(shift_sentence("it should shift the sentence"))
print(shift_sentence("the output is not very legible"))
print(shift_sentence("edabit"))


'''
shift_sentence("create a function") ➞ "freate c aunction"

shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"

shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"

shift_sentence("edabit") ➞ "edabit"
'''