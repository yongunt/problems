from string import ascii_lowercase as ALPHL # ALPHL stand for alphabet lower
from string import ascii_uppercase as ALPHU # ALPHL stand for alphabet upper

def caesar_encryption(message:str, shift:int) -> str:
  '''
  Caesar encryption
  '''

  message = list(message)

  for i in range(len(message)):
    if message[i] in ALPHL: message[i] = ALPHL[(ALPHL.index(message[i]) + shift) % 26]
    elif message[i] in ALPHU: message[i] = ALPHU[(ALPHU.index(message[i]) + shift) % 26]

  return "".join(message)
    

""" print(caesar_encryption("middle-Outz", 2)) """ #output: okffng-Qwvb
""" print(caesar_encryption("Always-Look-on-the-Bright-Side-of-Life", 5)) """ #output: Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj
""" print(caesar_encryption("A friend in need is a friend indeed", 20)) """ #output: U zlcyhx ch hyyx cm u zlcyhx chxyyx

check = "0"

while True:
  if check.lower() == "q": break

  try:
    print("")
    message = input("Please enter a message -> ")
    shift = input("How many time you wanna shift the letters -> ")
  
    try: print("Message succesfully encrypted -> ", caesar_encryption(str(message), int(shift)), "\n")
    except: print("Please enter a valid variables :)\n")

    check = input("If you wanna quit press 'q', otherwise press anything not being 'q'\n")

  except:
    print("Please enter a valid variables :)\n")
    check = input("If you wanna quit press 'q', otherwise press anything not being 'q'\n")