#isomorphic-strings
class Solution(object):
    def isIsomorphic(self, s, t):
        def encode_pattern(x):
            first = {}
            res = []
            next_id = 0

            for ch in x:
                if ch not in first:
                    first[ch] = next_id
                    next_id += 1
                res.append(first[ch])

            return res

        return encode_pattern(s) == encode_pattern(t)