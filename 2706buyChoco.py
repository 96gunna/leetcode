class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        cash = money - sum(sorted(prices)[:2])
        if cash >= 0:
            return cash
        else:
            return money
