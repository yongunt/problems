def overlap(first:str, second:str):
    f_holder = []
    s_holder = []
    common = ""
    current_len = 0

    for i in range(1, len(first) + 1): f_holder.append(first[::-1][:i][::-1])

    for i in range(1, len(second) + 1): s_holder.append(second[:i])

    for i in f_holder:
        if i in s_holder and len(i) > current_len:
            common = i
            current_len = len(i)

    first = first.replace(common, "")

    return first + second


print(overlap("sweden", "denmark"))
print(overlap("edabit", "iterate"))
print(overlap("honey", "milk"))
print(overlap("dodge", "dodge"))


'''
overlap("sweden", "denmark") ➞ "swedenmark"

overlap("edabit", "iterate") ➞ "edabiterate"

overlap("honey", "milk") ➞ "honeymilk"

overlap("dodge", "dodge") ➞ "dodge"
'''