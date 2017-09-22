while True:
	print("Enter 'x' for exit.")
	check = input("Are you a Robot ? ")
	if check == 'x':
		break
	elif check == 'yes' :
		print("Sorry!, you can not proceed.\n")
	else:
		print("Congrats!, you can proceed.\n")