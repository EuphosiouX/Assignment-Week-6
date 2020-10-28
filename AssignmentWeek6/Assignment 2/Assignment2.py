prices = {
          "banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3
         }

stock = {
         "banana": 6,
         "apple": 0,
         "orange": 32,
         "pear": 15
        }

total = 0

for x in prices and stock:
         print(x,"\nPrices:",prices.get(x),"\nStock:",stock.get(x))
         stock_and_price = prices.get(x)*stock.get(x)
         print("Total for",x + ":",stock_and_price,"\n")
         total += stock_and_price 

print("Grand total:",total)
