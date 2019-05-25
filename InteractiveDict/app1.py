import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("./data/data.json"))

def translate(word):
  temp = word.lower()

  if temp in data:
    return data[temp]
  elif temp.capitalize() in data:
    return data[temp.capitalize()]
  elif temp.upper() in data:
    return data[temp.upper()]
  elif len(get_close_matches(temp, data.keys(), cutoff=0.8)) != 0:
    yn = input(f"Did you mean {get_close_matches(temp, data.keys(), cutoff=0.8)[0]}? (Y|N): ")
    answer = yn.lower()
    
    while answer != "y" or answer != "n":
      answer = input("Please press y or n, q to quit")
      if answer == "y":
        return data[get_close_matches(temp, data.keys(), cutoff=0.8)[0]]
      elif answer == "n":
        return f"The {temp} is not in the dictionary, please double check."
      elif answer == "q":
        return f"Quitting.."
    
  else:
    return f"The {temp} is not in the dictionary, please double check."

word = str(input("Please input a word to search > "))

output = translate(word)

print(word.upper() + ":")
if type(output) == list:
  for item in output:
    print(item)
else:
  print(item)