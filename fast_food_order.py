from datetime import datetime
"""
Sipho
2020-04-21
cash_register.py
This program transforms a computer into a cash cash register
"""
print("Welcome to the cash register program.")
print("You will be entering the orders of customers.")

# Letter # Food # Cost # Quantity
food = [
	["H", "Hamburger", 1.29, 0],
	["O", "Onion Rings", 1.09, 0],
	["C", "Cheeseburger", 1.49, 0],
	["S", "Small Soft Drink", 0.79, 0],
	["F", "Fries", 0.99, 0],
	["L", "Large Soft Drink", 1.19, 0],
]
currency_symbol = "R"
VAT = 0.15


def menu(food_list=[]):
	"""
	A method for printing a menu list
	for customers to choose from.
	:argument list()
	:returns void
	"""
	print("Food Menu:")
	for item in food_list:
		print(f"{item[0]} - {item[1]}: {currency_symbol}{item[2]}, qty={item[3]}")
	pass


def get_quantity(item_name, qty=0):
	"""
	A method for prompting the user to enter required quantity
	:argument item_name (string), qty (number)
	:returns number
	"""
	while qty == 0:
		try:
			qty = int(input(f"How many {item_name}s would you like?: "))
			return qty
		except ValueError as err:
			print("Please enter a valid number!!")


def payment(total_amount=0.00):
	"""
	A method of collecting payment from a customer
	"""
	cash = 0.00
	while cash < total_amount:
		try:
			cash = float(input(f'Please enter a value greater than or equal to {currency_symbol} {total_amount} to pay for your products: '))
		except ValueError as err:
			print(err)

		if cash < total_amount:
			try:
				void = str(input(f'The amount you paid {currency_symbol} {cash} is less than the balance due {currency_symbol} {total_amount}.\nWould you like to void this transaction?\nType (yes/no): '))
				if void == 'yes':
					print('It\'s sad to see you leave empty handed :(\n We hope to see you next time :)')
					return False
			except ValueError as err:
				raise err
	return cash


def checkout(cart=[]):
	"""
	A method for calculating grand total
	:arg list
	:returns float
	"""
	SHOP_NAME = '**** McDonalds Cresta Mall ****'
	now = datetime.now()
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	sub_total = 0.00
	print(SHOP_NAME)
	print(f'Date:       {date_time}')
	print("\nReport of Sales: \nItem:\tQuantity\tSales")
	for item in cart:
		print(f"{item[0]}\t{item[1]} \t\t {currency_symbol} {str(item[2])}")
		sub_total += round(item[1]*item[2], 2)
	tax = round(sub_total * VAT, 2)
	grand_total = round(sub_total + tax, 2)
	print(f"\nTotal Sales: {currency_symbol}{sub_total}")
	print(f"Total Tax: {currency_symbol}{tax}")
	print(f"Grand Total: {currency_symbol}{grand_total}")
	amount_tendered = payment(grand_total)
	print(f"Amount Tendered: {amount_tendered}")
	change = round(amount_tendered - grand_total, 2)
	print(f"Change: {change}")


def order_selection():
	"""
	order selection method
	:returns list
	"""
	total_cost = 0
	cart = []
	match = 0
	menu(food)
	select = True
	while select:
		choice = input("Select a letter corresponding to the menu choice: ").upper()
		for item in food:
			if choice == item[0]:
				match += 1
				quantity = get_quantity(item[1])
				food_price = round(item[2] * quantity, 2)
				total_cost += food_price
				print(f"{item[1]}, \t {currency_symbol} {food_price}")
				entry = [item[1], quantity, food_price]
				cart.append(entry)
				done = input("Are you done with your selection?\nEnter (yes/no): ")
				if done == "yes":
					select = False
					break
		if match <= 0:
			print("Your entry is incorrect!!!!")
			select = True
	checkout(cart)


order_selection()