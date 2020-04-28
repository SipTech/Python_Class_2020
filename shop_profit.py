currency_symbol = 'R'

soap = {
  'cost_price': 32.67,
  'sell_price': 45.00,
  'inventory': 1200,
}

sunlight = {
  'cost_price': 225.89,
  'sell_price': 550.00,
  'inventory': 100,
}

candy = {
  'cost_price': 2.77,
  'sell_price': 7.95,
  'inventory': 8500,
}

def profit_rocket(product={}):
  """
  A simple reusable function for calculating product profit given a dictionary with the following key, value pairs:
  {
    cost_price: 0.00, 
    sell_price:0.00, 
    inventory:0.00
  }
  :args dict
  :returns float
  """
  total_cost = (
    product.get('cost_price') 
    * product.get('inventory')
  )
  stock_value = (
    product.get('sell_price') 
    * product.get('inventory')
  )
  return round((stock_value - total_cost),2)

print(f'Profit on soap: {currency_symbol} {profit_rocket(soap)}')
print(f'Profit on sunlight: {currency_symbol} {profit_rocket(sunlight)}')
print(f'Profit on candy: {currency_symbol} {profit_rocket(candy)}')