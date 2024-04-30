def discount(prices:list) -> list:
    if len(prices) >= 3:
        holder = []
        times = len(prices) // 3
        for i in range(times): holder.append(sorted(prices)[i])
        dc = (sum(holder) * 100) / sum(prices)
        for i in range(len(prices)): prices[i] = round(prices[i] - (prices[i] * (dc / 100)), 2)
    
    return prices


print(discount([2.99, 5.75, 3.35, 4.99]))
print(discount([10.75, 11.68]))
print(discount([68.74, 17.85, 55.99]))
print(discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]))


'''
discount([2.99, 5.75, 3.35, 4.99]) ➞ [2.47, 4.74, 2.76, 4.12]
# First product for free.

discount([10.75, 11.68]) ➞ [10.75, 11.68]
# No discounts applied.

discount([68.74, 17.85, 55.99]) ➞ [60.13, 15.62, 48.98]
# Second product for free.

discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]) ➞ [5.16, 13.45, 33.06, 10.91, 22.71, 5.16, 5.16, 5.16]
# First and sixth products for free (see second note).
'''      