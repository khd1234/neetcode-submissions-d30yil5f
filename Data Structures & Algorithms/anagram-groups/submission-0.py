class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - 97] += 1
            result_dict[tuple(count)].append(word)
        return list(result_dict.values())
