class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pm=[]
        n=len(prices)
        for i in range(n):
            for j in range(i+1,n):
                if prices[i]<prices[j]:
                    pm.append(prices[j]-prices[i])
        if len(pm)==0:
            return 0 
        else:
            return max(pm)           
        
