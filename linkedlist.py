
class Element :
	def __init__(self, key=None, value=None, pointer=None) :
		self.key = key
		self.value = value
		self.pointer = pointer

	def print_element(self) :
		print("key :", self.key, "value :", self.value, "next :", self.pointer)

	def copy(self) :
		return Element(self.key, self.value, None)

class LinkedList :
	def __init__(self, head=None) :
		self.head = head
		self.tail = head

	def elements_generator(self) :
		current = None
		while True :
			if self.head == None :
				break
			elif current == None :
				current = self.head
			elif current.pointer != None :
				current = current.pointer
			else :
				break
			yield current

	def elements_list(self) :
		my_list = []
		if self.head != None :
			current = self.head
			my_list.append(current)
			while current.pointer != None :
				current = current.pointer
				my_list.append(current)

		return my_list

	def full_print(self) :
		current = self.head
		while current != None :
			current.print_element()
			current = current.pointer

	def pointers_print(self) :
		print("head")
		if self.head != None :
			self.head.print_element()
		else :
			print(self.head)
		print("tail")
		if self.tail != None :
			self.tail.print_element()
		else :
			print(self.tail)

	def is_object(self, element) :
		current = self.head
		while current != None :
			if current == element :
				return True
			current = current.pointer
		return False

	def is_object_element(self, element) :
		current = self.head
		while current != None :
			if current == element :
				return (True, current)
			current = current.pointer
		return (False, None)

	def is_key(self, element) :
		current = self.head
		while current != None :
			if current.key == element.key :
				return True
			current = current.pointer
		return False

	def is_key_element(self, element) :
		current = self.head
		while current != None :
			if current.key == element.key :
				return (True, current)
			current = current.pointer
		return (False, None)

	def index_of(self, element) :
		current = self.head
		current_index = 0
		while current != None :
			if current == element :
				return current_index
			current = current.pointer
			current_index += 1
		return -1

	def pop(self, element) :
		if self.head == element :
			self.head = element.pointer
		else :
			current = self.head
			while current.pointer != None :
				if current.pointer == element :
					if current.pointer == self.tail :
						self.tail = current
					current.pointer = current.pointer.pointer
				current = current.pointer

	def pop_tail(self) :
		if self.head == None :
			pass
		elif self.head.pointer == None :
			self.head = None
			self.tail = None
		else :
			current = self.head
			while current.pointer.pointer != None :
				current = current.pointer
			current.pointer = None
			self.tail = current

	def pop_head(self) :
		if self.head != None :
			self.head = self.head.pointer


	def add_to_tail(self, element) :
		if self.head != None :
			current = self.head
			while current.pointer != None :
				current = current.pointer
			current.pointer = element
		else :
			self.head = element
		self.tail = element

	def add_to_head(self, element) :
		element.pointer = self.head
		self.head = element
		if self.head.pointer == None :
			self.tail = self.head

	def insert_at_index(self, index, element) :
		if index == 0 :
			self.add_to_head(element)
		else :
			current = self.head
			for i in range(index-1) :
				if current.pointer == None :
					return
				current = current.pointer
			element.pointer = current.pointer
			current.pointer = element
			if element.pointer == None :
				self.tail = element

	def len(self) :
		if self.head != None :
			current = self.head
			elements_counter = 1
			while current.pointer != None :
				current = current.pointer
				elements_counter += 1
			return elements_counter
		else :
			return 0


if __name__ == '__main__' :
	liste = LinkedList()
	a = Element("a", 1)
	b = Element("b", 2)
	c = Element("c", 3)
	d = Element("d", 4)

	liste.add_to_head(a)
	liste.add_to_tail(b)
	liste.add_to_tail(c)
	liste.insert_at_index(3, d)

	liste.pointers_print()
	liste.full_print()
