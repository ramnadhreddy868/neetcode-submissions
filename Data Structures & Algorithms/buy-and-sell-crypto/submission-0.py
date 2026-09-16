class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        maxprofit=0
        for i in range(left+1,len(prices)):
            profit=prices[i]-prices[left]
            maxprofit=max(maxprofit,profit)
            if prices[i] < prices[left]:
                left = i
            
        return maxprofit


        