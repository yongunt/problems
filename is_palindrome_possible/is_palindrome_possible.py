def is_palindrome_possible(word:str):
  flag = True
  holder = []

  for i in word:
    if word.count(i) % 2 != 0:
      flag = False
      holder.append(word.count(i))
      
  if flag:
    return True
  else:
    if len(holder) == 1: return True
    else: return False

print(is_palindrome_possible("rearcac"))
print(is_palindrome_possible("suhbeusheff"))
print(is_palindrome_possible("palindrome"))