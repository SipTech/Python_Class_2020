def get_payment(total_amount=0.00):
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


def map_letter_to_full_word(letter, list_of_words=[]):
	"""
	A function for mapping a letter to a word in a list
	:arg string, list()
	:return string
	"""
	for _choice in list_of_words:
		if _choice.startswith(letter.upper()) and len(_choice) > 1:
			return _choice