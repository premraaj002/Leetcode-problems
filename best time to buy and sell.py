#leetcode problem number : 121


prices=[7,1,5,3,6,4]
buy_price = prices[0]
profit = 0
for p in prices[1:]:
    print("P Value:",p)
    print("before Buy price:", buy_price)
    if buy_price > p:
        buy_price = p
    print("After Buy price:", buy_price)        
    profit = max(profit, p - buy_price)
    print("PROFIT:",profit)    
print (profit)