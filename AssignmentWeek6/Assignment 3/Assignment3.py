groceries = ["banana", "orange", "apple"]

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

def compute_bill(food):
    total = 0
    for items in food:
        if(stock.get(items)> 0):
            totals = prices.get(items)
            total += totals 
            stock[items]-=1
        else:
            print(items,"not in stock")
    return total

print("Total Bill:",compute_bill(groceries))
print("Final Stock:",stock)