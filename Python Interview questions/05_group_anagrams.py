# Q5. Given a list of strings, group them into lists of anagrams.

# pip intall collections
from collections import defaultdict

def group_anagrams(strings):
    anagrams = defaultdict(list)
    
    for string in strings:
        key = ''.join(sorted(string))
        anagrams[key].append(string)
    
    return list(anagrams.values())

input_strings = ["eat", "tea", "tan", "ate", "nat", "ball", "bat"]
print("Grouped anagrams:", group_anagrams(input_strings))
