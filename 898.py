class Solution:
    def subarrayBitwiseORs(self, arr):
        result = set()
        prev = set()

        for num in arr:
            curr = {num}
            for val in prev:
                curr.add(val | num)
            result.update(curr)
            prev = curr

        return len(result)
