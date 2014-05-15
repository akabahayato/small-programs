alphabet = ('abcdefghijklmnopqrstuvwxyz')

def x1(i,j,k):
	try:
		print alphabet[i]+alphabet[j]+alphabet[k]
		k+=1
		x1(i,j,k)
	except:
		
		"try:"
		x2(i,j,k)
		"""except :
			pass"""

			
def x2(l,m,n):
	try:
		print alphabet[l]+alphabet[m]+alphabet[n]
		m+=1
		x2(l,m,n)
	except:
		"try:"
		x3(l,m,n)
		"""except :
			pass"""

def x3(p,q,r):
	try:
		print alphabet[p]+alphabet[q]+alphabet[r]
		p+=1
		x3(p,q,r)
	except:
		"try:"
		x1(p,q,r)
		"""except :
			pass"""


			
try:
	x1(0,0,0)
except RuntimeError:
	print "break"