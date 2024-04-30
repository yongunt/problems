def find_pattern(phases:dict, word:str) -> list:
    ans:list = []
    
    for key in phases:
        if word.lower() in phases[key].lower(): ans.append(key + " = " + word)
        else: ans.append(key + " = None")

    return ans


print(find_pattern({
  "Phrase1": "COVID-19 is no good",
  "Phrase2": "COVID-18 is no good",
  "Phrase3": "COVID-17 is no good"
}, "COVID-19"))

print(find_pattern({
  "Phrase1": "Edabit is great",
  "Phrase2": "Edabit is very great",
  "Phrase3": "Edabit is really great"
}, "really"))


'''
find_pattern({
  "Phrase1": "COVID-19 is no good",
  "Phrase2": "COVID-18 is no good",
  "Phrase3": "COVID-17 is no good"
}, "COVID-19") ➞ ["Phrase1 = COVID-19", "Phrase2 = None", "Phrase3 = None"]

find_pattern({
  "Phrase1": "Edabit is great",
  "Phrase2": "Edabit is very great",
  "Phrase3": "Edabit is really great"
}, "really") ➞ ["Phrase1 = None", "Phrase2 = None", "Phrase3 = really"]
'''