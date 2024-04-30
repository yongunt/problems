def license_plate(plate:str, order:int) -> str:
    ans:str = ""
    plate:list = [i for i in plate if i != '-'][::-1]
    flag:bool = True

    for i in range(0, len(plate), order):
        for j in range(order):
            ans += plate[i]
            i += 1
            
            if i == len(plate):
                flag = False
                break
        
        if flag: ans += '-'

    return ans[::-1].upper()


print(license_plate("5F3Z-2e-9-w", 4))
print(license_plate("2-5g-3-J", 2))
print(license_plate("2-4A0r7-4k", 3))
print(license_plate("nlj-206-fv", 3))


'''
license_plate("5F3Z-2e-9-w", 4) ➞ "5F3Z-2E9W"

license_plate("2-5g-3-J", 2) ➞ "2-5G-3J"

license_plate("2-4A0r7-4k", 3) ➞ "24-A0R-74K"

license_plate("nlj-206-fv", 3) ➞ "NL-J20-6FV"
'''