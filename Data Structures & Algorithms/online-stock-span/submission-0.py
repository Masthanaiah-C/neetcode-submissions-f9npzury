class StockSpanner:

    def __init__(self):
        #initialise a stack which holds stock price and its span value
        self.SSpanner = list()


    def next(self, price: int) -> int:
        if (len(self.SSpanner) == 0):
            self.SSpanner.append([price, 1])
            return 1
        else:
            count = 1
            while(len(self.SSpanner) and self.SSpanner[-1][0] <= price):
                popS = self.SSpanner.pop()
                count += popS[1]
            self.SSpanner.append([price, count])
            return count




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)