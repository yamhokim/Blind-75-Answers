'''
Approach without sorting strings - O(N * M)
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        palindromes = {}
        for string in strs:
            letter_counts = [0]*26
            for letter in string:
                index = ord(letter) - ord('a')
                letter_counts[index] += 1
            if str(letter_counts) in palindromes:
                palindromes[str(letter_counts)].append(string)
            else:
                palindromes[str(letter_counts)] = [string]
        
        return [group for group in palindromes.values()]
    

'''
Approach using sorted strings - O(N * MlogM)
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        palindromes = {}
        for string in strs:
            sorted_str = sorted(string)
            if str(sorted_str) in palindromes:
                palindromes[str(sorted_str)].append(string)
            else:
                palindromes[str(sorted_str)] = [string]

        return [group for group in palindromes.values()]