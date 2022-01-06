class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def if_repeat(corpus, patt):
            corpus_length = len(corpus)
            patt_length = len(patt)
            if corpus_length % patt_length != 0: return False
            beg, end = 0, patt_length-1
            while end < corpus_length:
                if patt != corpus[beg:end+1]: return False
                beg, end = beg + patt_length, end + patt_length
            return True
        ans = ""
        longest = 0
        len1, len2 = len(str1), len(str2)
        if len1 > len2 : return self.gcdOfStrings(str2, str1)
        pattern = ""
        for letter in str1:
            pattern += letter
            if if_repeat(str1, pattern) and if_repeat(str2, pattern):
                pattern_length = len(pattern)
                if pattern_length > longest:
                    ans, longest = pattern, pattern_length
        return ans