Oddly or Evenly Positioned From Last
Create a function that extracts the characters from a list (or a string) on odd or even positions, depending on the specifier. The string "odd" for items on odd positions (... 5, 3, 1) and "even" for even positions (... 6, 4, 2) from the last item of that list or string.

Examples
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 4th & 2nd positions from right.

char_at_pos("EDABIT", "odd") ➞ "DBT"
# "D", "B" and "T" occupy the 5th, 3rd and 1st positions from right.

char_at_pos([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "odd") ➞ ["(", "&", "%", "#", "!"]

source --> https://edabit.com/challenge/72KukSssxk2eHrWqx