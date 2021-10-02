class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=999999
        
        if len(prices)==1 or len(prices)==0:
            return 0
        for stockPrice in prices:
            if stockPrice<buy:
                buy=stockPrice
            if stockPrice-buy>profit:
                profit=stockPrice-buy
        return profit