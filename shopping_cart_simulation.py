# Shopping Cart Solution
from random import choices
from datetime import datetime

number_of_items_to_pick = 7
catalog = {
	'Bread': 12.59,
	'Milk - 6 pack': 69.59,
	'Milk - 2Lt': 22.55,
	'Rice - 1kg': 25.00,
	'Mealie - Meal 10kg': 85.90,
	'Cooking oil - 2Lt': 25.59,
	'Chicken mixed portion - 5kg': 105.59,
	'Macaroni - 1kg': 13.59,
	'Sparghetti - 500g': 12.59,
	'Stewing beef - 1kg': 50.00,
	'Tomatoes - 1kg': 25.00,
	'Onions - 1kg': 35.00,
	'Butter': 40.00,
}

def shop_items(catalog, pick=6):
	"""
	A function that simulates a customer choosing items inserting them in a shopping cart.
	"""
	shopping_cart = []
	shopping_cart.append(choices(list(catalog.keys()), k=pick))
	return shopping_cart

def add_shopping_bag(items=[], amount=0.00, product_count=4):
	"""
	A method for asking a user if they'd like to add a shopping bag.
	"""
	user_input = None
	print(f'You have selected {product_count} items:')
	count = 0
	for item in items:
		print(f"{count}. {item}")
		count += 1
	while user_input not in ('yes', 'no'):
		user_input = input(f'Would you like to add a shopping bag @ R{amount} each? (yes/no): ')

	if user_input == 'yes':
		return True
	return False

def payment(total_amount=0.00):
	"""
	A method of collecting payment from a customer
	"""
	cash = 0.00
	while cash < total_amount:
		try:
			cash = float(input(f'Please enter a value greater than or equal to R{total_amount} to pay for your products: '))
		except ValueError as err:
			print(err)

		if cash < total_amount:
			try:
				void = str(input(f'The amount you paid R{cash} is less than the balance due R{total_amount}.\nWould you like to void this transaction?\nType (yes/no): '))
				if void == 'yes':
					print('It\'s sad to see you leave empty handed :(\n We hope to see you next time :)')
					return False
			except ValueError as err:
				raise err
	return cash

def checkout(products):
	"""
	A function that accepts payment from a user after working out the total amount.
	"""
	SHOP_NAME = 'Checkers Cresta Mall'
	VAT = 0.15
	SHOPPING_BAG = 00.50
	cart_total = 0.00
	now = datetime.now()
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	cart = shop_items(products, number_of_items_to_pick)[0]
	item_count = 0
	group_items = []
	for item in cart:
		cart_total += round(products[item], 2)
		print(f'Total: {round(cart_total, 2)}')
		# every group of nth items needs a shopping bag
		if item_count == 3:
			if add_shopping_bag(items=group_items, amount=SHOPPING_BAG, product_count=item_count):
				cart_total += round(SHOPPING_BAG, 2)
			# reset item count on every nth count
			group_items.clear()
			item_count = 0
		group_items.append(item)
		# increment item count
		item_count += 1

	balance_due = round((cart_total * VAT) + cart_total, 2)
	amount_tendered = round(payment(balance_due), 2)
	if amount_tendered:
		change = round(amount_tendered - balance_due, 2)
		print(f'**** {SHOP_NAME} ****')
		print(f'Date:       {date_time}')
		print('Item     Amount')
		for item in cart:
			for key, value in products.items():
				if key == item:
					print(f"{key}:                  R{value}")
		print(f'Sub Total:      R{round(cart_total, 2)}')
		print(f'VAT:            R{VAT}')
		print(f'Balance Due:    R{balance_due}')
		print(f'Amount Tendered:R{amount_tendered}')
		print(f'Change:        :R{change}')

checkout(catalog)