class S_node:
	def __init__(self, new_data):
		self.data = new_data
		self.next = None

class List_manager:
	def __init__(self, head):
		self.head = head
		self.count = 1

	def append(self, new_node):
		if self.head == None:
			self.head = new_node
		else:
			tmp = self.head
			while tmp.next != None:
				tmp = tmp.next
			tmp.next = new_node
			self.count += 1
	
	def remove(self, remove_node):
		if self.head == None:
			return None
		if self.head == remove_node:
			self.head = self.head.next
			return True
		tmp = self.head
		while tmp.next and tmp.next != remove_node:
			tmp = tmp.next
			if tmp == None:
				return None
		tmp.next = tmp.next.next
		self.count -= 1
		return True
	
	def print_node(self):
		tmp = self.head
		while tmp:
			print(tmp.data)
			tmp = tmp.next
		return True

	def index_at(self, index):
		tmp = self.head
		i = 0
		if tmp is None:
			print("wrong input")
			return None
		if self.count - 1 < index:
			print("out of range!")
			return False
		while tmp.next and i < index:
			tmp = tmp.next
			i += 1
		return tmp

	def find_data(self, data):
		if self.head == None:
			print("wrong input")
			return None
		tmp = self.head
		while tmp.data != data:
			tmp = tmp.next
		if tmp == None:
			print("wrong input")
			return False
		return tmp

	def insert_after(self, here, new_node):
		if here == None or new_node == None:
			print("wrong input" )
			return None
		new_node.next = here.next
		here.next = new_node
		self.count += 1
		return True

	def insert_before(self, here, new_node):
		if self.head == None or here == None or new_node == None:
			print("wrong input")
			return None
		tmp = self.head
		while tmp.next != here:
			tmp = tmp.next
		new_node.next = here
		tmp.next = new_node
		self.count += 1
		return True
	
	def remove_all(self):
		if self.head == None:
			print("wrong input")
			return None
		node = self.head
		while node.next:
			tmp = node
			node = node.next
			tmp.next = None
		return True



print("-------------------[TEST]----------------------")
print("-------------------[GOGO]----------------------")

print
print
print

print("------------------[CREATE]---------------------")
one_node = S_node(1)
new_list = List_manager(one_node)
new_list.print_node()
print("count is ... ", new_list.count)

print("------------------[APPEND]---------------------")
two_node = S_node(2)
new_list.append(two_node)
new_list.print_node()
print("count is ... ", new_list.count)

print("------------------[APPEND]---------------------")
three = S_node(3)
new_list.append(three)
new_list.print_node()
print("count is ... ", new_list.count)

print("------------------[APPEND]---------------------")
four = S_node(4)
new_list.append(four)
new_list.print_node()
print("count is ... ", new_list.count)

print("------------------[AFTER]-----------------------")
two_quater = S_node(2.25)
new_list.insert_after(two_node, two_quater)
new_list.print_node()
print("count is ... ", new_list.count)

print("------------------[BEFORE]----------------------")

two_half = S_node(2.5)
new_list.insert_before(three, two_half)
new_list.print_node()
print("count is ... ", new_list.count)

print("-----------------[FIND DATA]--------------------")

print(new_list.find_data(2.5).data)
print("-----------------[FIND INDEX]-------------------")

print(new_list.index_at(3).data)
print("------------------[THE END]---------------------")
