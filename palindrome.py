def is_palindrome_with_punctuation(str):
	"""Checking if a string with punctuation is a palindrome
	"""
	s = 0
	e = len(str) - 1
	while s <= e:
		while not str[s].islower():
			s += 1
		while not str[e].islower():
			s -= 1
		if str[s] != str[e]:
			return False
	return True

def same(r1, r2):
	"""Checking if two trees are equivalent and have the same structure
	"""
	if not r1 and not r2:
		return True
	if (not (r1 and r2)) and (not (r2 and r1)): # EXCLUSIVE OR
		return False
	return r1.val == r2.val and same(r1.left, r2.left) \
	and same(r1.right, r2.right)
	# you can also traverse the trees (breadth-first) and check
	# as you go	

def dft(n):
	if not n:
		return
	# prints the whole thing in order; pre-order traversal
	print n.val
	dft(n.left)
	# a print statement here prints the whole thing out, collapsed
	# left to right; called in order traversal
	# if it's a binary search tree, this gives you the elements
	# in order
	dft(n.right)
	# prints on the way up the right side; post-order traversal