class Solution:
    def play(self, nums, start, end, p, totalSum, bestScoreMemo):
        if start > end:
            return 0

        if (start, end, p) in bestScoreMemo:
            return bestScoreMemo[start, end, p]

        if p == "p1":
            p2MaxScore1 = self.play(
                nums, start + 1, end, "p2", totalSum - nums[start], bestScoreMemo
            )
            p2MaxScore2 = self.play(
                nums, start, end - 1, "p2", totalSum - nums[end], bestScoreMemo
            )
            bestScoreMemo[start, end, p] = max(
                totalSum - p2MaxScore1, totalSum - p2MaxScore2
            )
        else:
            p1MaxScore1 = self.play(
                nums, start + 1, end, "p1", totalSum - nums[start], bestScoreMemo
            )
            p1MaxScore2 = self.play(
                nums, start, end - 1, "p1", totalSum - nums[end], bestScoreMemo
            )
            bestScoreMemo[start, end, p] = max(
                totalSum - p1MaxScore1, totalSum - p1MaxScore2
            )

        return bestScoreMemo[start, end, p]

    def predictTheWinner(self, nums: List[int]) -> bool:
        bestScoreMemo = {}
        total_sum = sum(nums)
        self.play(nums, 0, len(nums) - 1, "p1", total_sum, bestScoreMemo)
        p1BestScore = bestScoreMemo[(0, len(nums) - 1, "p1")]
        return p1BestScore >= total_sum - p1BestScore
