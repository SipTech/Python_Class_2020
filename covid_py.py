import time
covid = True
lock_down = 21
lock_down_day = 0
covid_infections = 100000
sleep_time_between_iterations = 2.5 #seconds

while covid and lock_down_day <= lock_down:
	lock_down_days_left = lock_down - lock_down_day
	print("Day: {0}, number of infections in RSA {1}".format(lock_down_day, covid_infections))

	if lock_down_day == 4:
		covid_infections -= 5000
		print("Covid 19 infections have dropped down to {0}".format(covid_infections))

	if lock_down_day == 13:
		covid_infections -= 60000
		print("large numbers of infected people are recovering..")
		print("Covid 19 infections have dropped down to {0}".format(covid_infections))

	if lock_down_day == 17:
		covid_infections -= 30000
		print("Covid 19 infections have dropped down to {0}".format(covid_infections))

	if lock_down_days_left == 4:
		print("Yey!! {0} more day to freedom".format(lock_down_days_left))

	if covid_infections < 1000:
		print("Hooray!!! Government finally announced, lockdown period is finally over.")
		covid = False
	else:
		print("Mmm!! We still have {0} days of lockdown..".format(lock_down_days_left))
		print("Number of infections are still high...\n")
		covid_infections -= 200

	lock_down_day += 1

	time.sleep(sleep_time_between_iterations)
