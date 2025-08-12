class Solution:
    def remove_pair(self, s, a, b, points):
        stack = []
        score = 0
        for ch in s:
            if stack and stack[-1] == a and ch == b:
                stack.pop()
                score += points
            else:
                stack.append(ch)
        return "".join(stack), score

    def maximumGain(self, s, x, y):
        if x > y:
            s, score1 = self.remove_pair(s, 'a', 'b', x)
            _, score2 = self.remove_pair(s, 'b', 'a', y)
        else:
            s, score1 = self.remove_pair(s, 'b', 'a', y)
            _, score2 = self.remove_pair(s, 'a', 'b', x)

        return score1 + score2
