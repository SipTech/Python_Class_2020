"""
FizzBuzz
"""

# loop from 0 to 100
for number in range(10):
	# check if the number is divisible by 2 and leaves no remainder
	if number % 2 == 0:
		# If it leave no remainder print Fizz
		print("Fizz is {0} whole number".format(number))
	else:
		# otherwise (else/ or else) print Buzz
		print("Buzz is {0} I am a PRIME".format(number))
