def identify(floor3:list = [], floor2:list = [], floor1:list = []) -> str:
    cubes:list = floor3 + floor2 + floor1
    if len(cubes) == 0: return None
    if len(cubes) == 9: return "Full"
    elif len(cubes) % 3 == 0: return "Non-Full"
    else:
        remaning:int = 9 - len(cubes) 
        return "Missing " + str(remaning)


print(identify(
  ["O", "O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]
))

print(identify(
  ["O", "O", "O"],
  ["O", "O", "O"]
))

print(identify(
  ["O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]
))


'''
identify(
  ["O", "O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]
) ➞ "Full"

# This is 3x3 full Rubik's Cube.
# So we should return "Full"
identify(
  ["O", "O", "O"],
  ["O", "O", "O"]
) ➞ "Non-Full"

# This is a 2x3 Rubik's Cube.
# It's not full, so we should return "Non-Full".
identify(
  ["O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]
) ➞ "Missing 1"

# This is almost a 3x3 Rubik's Cube with one missing part.
# We should return "Missing 1".
'''