class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        freq_dic_s, freq_dic_t = {}, {}
        for c in s:
            freq_dic_s[c] = freq_dic_s.get(c, 0) + 1
        
        for c in t:
            freq_dic_t[c] = freq_dic_t.get(c, 0) + 1

        return freq_dic_s == freq_dic_t