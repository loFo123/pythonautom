# import time
#
# for i in range(10):
#     print(i)
#     time.sleep(1)
import re
from datetime import date


def compare_strings(string1, string2):
  #Convert both strings to lowercase
  #and remove leading and trailing blanks
  string1 = string1.lower().strip()
  string2 = string2.lower().strip()

  #Ignore punctuation
  punctuation = "[.?!,;:'-]"
  string3 = re.sub(punctuation,r"", string1)
  string4 = re.sub(punctuation,r"", string2)

  #DEBUG CODE GOES HERE
  # print(string4)
  # print(string3)

  return string3 == string4

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False

today = date.today();
print(today.strftime( r"%Y-%m-%d"))
