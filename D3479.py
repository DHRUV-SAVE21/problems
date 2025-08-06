#3479. Fruits Into Baskets III
class SegmentTree:
    def __init__(self, baskets):
        self.n = len(baskets)
        self.max = [0] * (4 * self.n)
        self.buildTree(1, 0, self.n - 1, baskets)

    def buildTree(self, treeIdx, left, right, baskets):
        if left == right:
            self.max[treeIdx] = baskets[left]
            return
        mid = (left + right) // 2
        self.buildTree(2 * treeIdx, left, mid, baskets)
        self.buildTree(2 * treeIdx + 1, mid + 1, right, baskets)
        self.updateParent(treeIdx)

    def updateParent(self, treeIdx):
        self.max[treeIdx] = max(self.max[2 * treeIdx], self.max[2 * treeIdx + 1])

    def placeFruit(self, treeIdx, left, right, size):
        if self.max[treeIdx] < size:
            return False
        if left == right:
            self.max[treeIdx] = -1  # Only 1 fruit per basket
            return True
        mid = (left + right) // 2
        placed = self.placeFruit(2 * treeIdx, left, mid, size)
        if not placed:
            placed = self.placeFruit(2 * treeIdx + 1, mid + 1, right, size)
        self.updateParent(treeIdx)
        return placed


class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        if not baskets:
            return len(fruits)

        tree = SegmentTree(baskets)
        unplaced = 0

        for fruit in fruits:
            placed = tree.placeFruit(1, 0, len(baskets) - 1, fruit)
            if not placed:
                unplaced += 1

        return unplaced
