def make_str(x): return str(x)


def custom_sort(rule, word):
    result = ""
    holder = ""

    for letter in word:
        if letter not in rule: holder += letter

    for letter in sorted(holder): result += letter

    return rule + result


print(custom_sort("edc", "abcdefzyx"))
print(custom_sort("fby", "abcdefzyx"))
print(custom_sort("", "abcdefzyx"))
print(custom_sort("", ""))


'''
custom_sort("edc", "abcdefzyx") ➞ "edcabfxyz"

custom_sort("fby", "abcdefzyx") ➞ "fbyacdexz"

custom_sort("", "abcdefzyx") ➞ "abcdefxyz"

custom_sort("", "") ➞ ""
'''