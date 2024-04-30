from string import ascii_lowercase as ALP

VOWELS = "aeiou"

def first_letter_to_end(word:str):
    word = list(word)

    if word[0].upper() == word[0]:
        holder = word[0].lower()
        del word[0]
        word[0] = word[0].upper() 
        return "".join(word) + holder
    else:
        holder = word[0]
        del word[0] 
        return "".join(word) + holder


def translate_word(word:str):
    if word == "": return ""

    if word[0].lower() not in VOWELS:
        while word[0].lower() not in VOWELS: word = first_letter_to_end(word)
        return word + "ay"
    else: return word + "yay"


def translate_sentence(sentence:str):
    sentence = sentence.split(" ")
    holder = ""
    non_letter = ""

    for i in range(len(sentence)):
        for j in sentence[i]:
            if j.lower() in ALP: holder+=j
            else: non_letter+=j
    
        sentence[i] = translate_word(holder) + non_letter

        holder = ""
        non_letter = ""

    return " ".join(sentence)


print(translate_word("flag"))
print(translate_word("Apple"))
print(translate_word("button"))
print(translate_word(""))
print(translate_sentence("I like to eat honey waffles."))
print(translate_sentence("Do you think it is going to rain today?"))