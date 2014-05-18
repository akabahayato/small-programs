"""
============================================================
				WORK IN PROGRESS
============================================================
an idiot builds a query engine 
in python 2.x
v0.1 [INCOMPLETE] 13/5/14

parts -----> identify parts of speech
	|
	---> identify type of question
		
(c) 2014, akabahayato @ (http://akabahayato.wordpress.com)
============================================================
SAMPLE QUERIES
============================================================
"What is a compiler?"
"What is the first day of the week
"What is the current stock price of Microsoft?"
"How many continents are there on earth?"
"How far is Paris from Brussels?"
"Who was the second man on the moon?" => Buzz Aldrin
"How do you make a 
"Where is the Eiffel Tower?"
"When was the first airplane built?"

so far,

what + (is/was) + (the/a)-> quantity, event, definition
how + [adj.] -> distance, quantity
how + [v] -> method
who -> identity
where -> location
when -> time

============================================================
LOG
============================================================

v0.01, 13/5 - Git test.
v0.01, 14/5 - Stuff
"""

class aiba_qe:

	w5h = ['who','what','why','when','where','how']
	
	def w5h_check(x):
		for i in w5h:
			if i == x:
				return i
	
			else:
				return 0
				
	def mainf(str):
		w5h_res = w5h_check(str.split(" ",1)[0])