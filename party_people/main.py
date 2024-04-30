def party_people(people:list) -> int:
    is_on:bool = True
    
    while is_on:
        if len(people) == 0: break

        for i in range(len(people)):
            is_on = False
            if people[i] > len(people):
                people.pop(i)
                is_on = True
                break

    return len(people)


print(party_people([4, 5, 4, 1]))
print(party_people([10, 12, 15, 15, 5]))
print(party_people([2, 1, 2, 0]))


'''
party_people([4, 5, 4, 1]) ➞ 1
# Ava's minimum number is 4, Mark's is 5, Sheila's is 4, and Pete's is 1.
# Only 1 person (Pete) stays.

party_people([10, 12, 15, 15, 5]) ➞ 0

party_people([2, 1, 2, 0]) ➞ 4
'''