from string import ascii_lowercase as ALPHABET
VOWELS = "aeiou"


def start_end(seq:str) -> bool:
    if (seq[0].lower() not in VOWELS) and (seq[-1].lower() not in VOWELS): return True
    return False


def vowel_order(seq:str) -> bool:
    seq = ''.join([i for i in seq if i != '-'])

    for i in range(1, len(seq)):
        if ((seq[i-1].lower() in VOWELS) and (seq[i].lower() in VOWELS)) or ((seq[i-1].lower() not in VOWELS) and (seq[i].lower() not in VOWELS)): return False
    return True


def skewer_count(seq:str) -> bool:
    skewer_count:int = 0
    holder:list = []

    for i in range(len(seq)):
        if seq[i].lower() in ALPHABET:
            for j in range(i + 1, len(seq)):
                if seq[j] == '-': skewer_count+=1
                if seq[j].lower() in ALPHABET:
                    holder.append(skewer_count)
                    skewer_count = 0
                    break

    for i in holder[1::]:
        if holder[0] != i: return False

    return True


def is_authentic_skewer(seq:str) -> bool:    
    flag:bool = True
    for i in seq:
        if i.lower() in ALPHABET: flag = False
    if flag: return False
    
    if '-' not in seq: return False
    
    if start_end(seq) and vowel_order(seq) and skewer_count(seq): return True
    
    return False


print(is_authentic_skewer("B--A--N--A--N--A--S"))
print(is_authentic_skewer("A--X--E"))
print(is_authentic_skewer("C-L-A-P"))
print(is_authentic_skewer("M--A---T-E-S"))
print(is_authentic_skewer("-------"))
print(is_authentic_skewer("FRIENDS"))


'''
is_authentic_skewer("B--A--N--A--N--A--S") ➞ True

is_authentic_skewer("A--X--E") ➞ False
# Should start and end with a consonant.

is_authentic_skewer("C-L-A-P") ➞ False
# Should alternate between consonants and vowels.

is_authentic_skewer("M--A---T-E-S") ➞ False
# Should have consistent spacing between letters.
'''