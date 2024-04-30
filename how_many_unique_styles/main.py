def unique_styles(styles:list) -> int: return len(set((','.join(styles)).split(',')))


print(unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]))

print(unique_styles([
  "Soul",
  "House,Folk",
  "Trance,Downtempo,Big Beat,House",
  "Deep House",
  "Soul"
]))


'''
unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]) ➞ 9

unique_styles([
  "Soul",
  "House,Folk",
  "Trance,Downtempo,Big Beat,House",
  "Deep House",
  "Soul"
]) ➞ 7
'''