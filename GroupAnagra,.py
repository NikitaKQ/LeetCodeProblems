from collections import defaultdict 
def groupAnagrams(strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
                

data = input().split()
print(groupAnagrams(data))