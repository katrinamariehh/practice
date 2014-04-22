# LINKED LISTS, BITCHES
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def append(data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	def get (Node, n):
		current = Node
		for i in range(1, n-1):
			next = current.next
			current = next
		return current

	def reverse(self):
	if self.head.next == None or self.head == None:
		break
	a = self.head
	b = a.next
	c = b.next

	a.next = None
	b.next = a
	a = b

	while c != None:
		b = c
		c = c.next
		b.next = a
		a = b
	self.head = b

	def recursive_reverse(self, node):
		temp = None
		if not node.next:
			return node
		else:
			temp = recursive_reverse(node.next)
			node.next.next = node
			node.next = None
		return temp

	def reverse_me(self):
		self.head = self.recursive_reverse(self.head)

# take an encoded string 'a5b6c15' and decode it
# 'aaaaabbbbbbccccccccccccccc'
def run_length_decoding(encoded_sequence):
	decoded_string = ''
	current_char = ''
	str_pairs_list = []
	pair_string = ''
	for c in encoded_sequence:
		if c.islower():
			print c
			if not pair_string == '':
				str_pairs_list.append(pair_string)
				pair_string = c
			else:
				pair_string = c
		elif c.isdigit():
			pair_string += c
	str_pairs_list.append(pair_string)
	print str_pairs_list
	for pair in str_pairs_list:
		decoded_string += pair[0] * int(pair[1:])
	return decoded_string



print run_length_decoding('a5b6c15')



# The hundred chairs problem:
# 100 chairs in a circle numbered 1-100
# kind of like musical chairs
# person 1 asked to leave
# person 2 stays
# person 3 leaves
# person 4 stays
# ...
# continue around the circle until only 1 person is left
# what # chair are they sitting in?

given node and LinkedList

def make_circular(self):
	self.tail.next = self.head

def rm_circular(self):
	this = self.tail
	while this.next != this:
		this.next = this.next.next
		this = this.next
	return this.data
	






			