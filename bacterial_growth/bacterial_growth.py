def bacteria(needed_mass:int) -> int:
    mass_of_one:int = 1
    mass_of_all:int = 1
    day:int = 0
    count_of_bacteria:int = 1

    while needed_mass > mass_of_all:
        day += 1

        # Morning
        count_of_bacteria *= 2
        mass_of_one = mass_of_all / count_of_bacteria

        # Night
        mass_of_one += 1
        mass_of_all = count_of_bacteria * mass_of_one

    return day


print(bacteria(9))
print(bacteria(16))
print(bacteria(548))
print(bacteria(5467))


'''
bacteria(9) ➞ 3

bacteria(16) ➞ 4

bacteria(548) ➞ 9

bacteria(5467) ➞ 12
'''