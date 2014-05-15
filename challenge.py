alphabet = list('abcdefghijklmnopqrstuvwxyz')

def main(i):
	try:
		print alphabet[i-1]*i
		i+=1
		main(i)
	except IndexError:
		pass
		

main(1)