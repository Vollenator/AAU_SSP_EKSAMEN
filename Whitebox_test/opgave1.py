def checkInputValue(value):
	if (value>3):
		if (value<10):
			print("Value is larger than 3 and smaller than 10")
			return "Value is larger than 3 and smaller than 10"
		else:
			print("Value is larger than or equal to 10")
			return "Value is larger than or equal to 10"
	else:
		if (value<0):
			print("Value is negative")
			return "Value is negative"
		else:
			print("Value is between zero and three")
			return "Value is between zero and three"


if __name__ == "__main__":
	valToBeChecked = [-5, -0.4, 0, 0.7, 1, 4, 3452, 10, 3]

	for i in valToBeChecked:
		print('For value '+str(i))
		checkInputValue(i)

