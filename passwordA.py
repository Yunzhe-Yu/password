password = "a123456"
i = 3
while i > 0:
	pwd = input('Please enter your password:')
	if pwd == password:
		print('Login Success!')
		break #out of loop
	else:
		i = i - 1
		if i == 0:
			print('System Locked!')
			break
		print('Wrong Password! You only have', i,'times!')
