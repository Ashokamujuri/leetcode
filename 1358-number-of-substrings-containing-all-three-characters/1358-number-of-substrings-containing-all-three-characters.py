class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        for right, char in enumerate(s):
            last_seen[char] = right
            min_idx = min(last_seen['a'], last_seen['b'], last_seen['c'])
            count += min_idx + 1
        return count