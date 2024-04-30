from string import ascii_lowercase as ALP

def find_base(word:str) -> int:
    biggest_letter_index:int = 0
    for letter in word:
        holder:int = ALP.index(letter) + 1
        if biggest_letter_index < holder: biggest_letter_index = holder
    return biggest_letter_index + 10


def create_base_numbers(base:int) -> dict:
    holder:list = [ALP[n] for n in range(base-10)]
    mydict:dict = {}
    for n in range(len(holder)): mydict[holder[n]] = n + 10
    return mydict


def word_to_decimal(word:str) -> int:
    word = word.lower()
    base:int = find_base(word)
    base_nums:dict = create_base_numbers(base)
    ans:int = 0
    for n in range(1, len(word)+1): ans += (base_nums[word[n-1]] * (base ** (len(word)-n)))
    return ans


print(word_to_decimal("Edabit"))
print(word_to_decimal("Python"))
print(word_to_decimal("ZERO"))


'''
word_to_decimal("Edabit") ➞ 351010469
# The highest letter of "Edabit" in the alphabet is "t"
# "t" is the 20th letter of the alphabet: adding 10 the result is 30
# "Edabit" in base-30 is equal to 351010469 in base-10

word_to_decimal("Python") ➞ 1365333188
# The highest letter of "Python" in the alphabet is "y"
# "y" is the 25th letter of the alphabet: adding 10 the result is 35
# "Python" in base-35 is equal to 1365333188 in base-10

word_to_decimal("ZERO") ➞ 1652100
# The highest letter of "ZERO" in the alphabet is "Z"
# "Z" is the 26th letter of the alphabet: adding 10 the result is 36
# "ZERO" in base-36 is equal to 1652100 in base-10
'''