password = 'a123456'
x = 0
while x < 3:
	code = input('Please enter your password:')
	if code == password:
		print('Login Success!')
		break
	elif code != password:
		print('Wrong Password! You only have', 2-x, ' times to try!')
	x = x + 1
else:
		print('System Locked!')