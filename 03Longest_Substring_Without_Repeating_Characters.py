class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        di = {}
        ans_li = []
        for i in range(len(s)):
            if di.get(s[i]):
                ans_li.append(len(di))
                new_idx = di[s[i]]
                di = {}
                for j in range(new_idx, i+1):
                    di[s[j]] = j+1
            else:
                di[s[i]] = i+1
        ans_li.append(len(di))
        return max(ans_li)