class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #creating a default dict that stores sorted word as a key
        anagram_storage = defaultdict(list)
        #going through loop and using the sorted word as a key and appending the word as a value
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_storage[sorted_word].append(word)
        #returning in the desired format
        return [anagrams for key,anagrams in anagram_storage.items()]
