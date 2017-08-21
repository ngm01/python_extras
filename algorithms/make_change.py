def change(cents):
	coins = {}
	# per stack overflow Python 2.x auto-truncates division to integers and has to be forced
	# to return a floating-point. If I remember rightly this isn't the case in Python 3, so I'm
	# using the double-division sign, which I think is the Python 3 way of forcing inteer divison.
	coins['dollars'] = cents // 100
	coins['quarters'] = (cents % 100) // 25
	coins['dimes'] = ((cents % 100)% 25) // 10
	coins['nickles'] = (((cents % 100)% 25) % 10) // 5
	coins['pennies'] = ((((cents % 100)% 25) % 10) % 5)

	return coins

counting = True
while counting:
	pennies_in_couch = raw_input("Enter some number of pennies, or q to quit. ")
	if pennies_in_couch == 'q':
		counting = False
		print "Bye"
		break
	else:
		try:
			print change(int(pennies_in_couch))
		except ValueError:
			print "That's not a number."

