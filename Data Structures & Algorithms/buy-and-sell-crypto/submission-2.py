class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        
        # Start our "lowest price" at infinity so the very first day 
        # is guaranteed to become our new lowest price.
        lowest_price = float('inf') 
        
        # ONE single loop!
        for today_price in prices:
            
            # SCENARIO A: We found a new, cheaper day to buy!
            if today_price < lowest_price:
                lowest_price = today_price
                
            # SCENARIO B: We didn't find a cheaper price, so let's see 
            # how much money we would make if we sold today.
            else:
                curr_profit = today_price - lowest_price
                
                # If today's profit beats our record, save it!
                if curr_profit > max_profit:
                    max_profit = curr_profit
                    
        return max_profit