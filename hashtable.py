
from linkedlist import *
import string

class HashTable :
	def __init__(self, size) :
		self.size = size
		self.list = self.init_list()
		self.nb_of_item = 0
		self.load_factor = 0

	def init_list(self) :
		tmp_list = []
		for i in range(self.size) :
			tmp_list.append(LinkedList())
		return tmp_list

	def add_element(self, key, value=None) :
		element = Element(key, value)
		key_index = hash(key)%self.size
		(element_exist, element_pointer) = self.list[key_index].is_key_element(element)
		if not element_exist :
			self.list[key_index].add_to_tail(element)
		else :
			element_pointer.value = element.value

	def remove_element(self, key) :
		element = Element(key, value)
		key_index = hash(key)%self.size
		(element_exist, element_pointer) = self.list[key_index].is_key_element(element)
		if element_exist :
			self.list[key_index].pop(element_pointer)

	def does_exist(self, key) :
		element = Element(key)
		key_index = hash(key)%self.size
		(element_exist, _) = self.list[key_index].is_key_element(element)
		return element_exist

	def get_value(self, key) :
		element = Element(key)
		key_index = hash(key)%self.size
		(element_exist, element_pointer) = self.list[key_index].is_key_element(element)
		if element_exist :
			return element_pointer.value
		else :
			return None

	def set_value(self, key, value) :
		element = Element(key, value)
		key_index = hash(key)%self.size
		(element_exist, element_pointer) = self.list[key_index].is_key_element(element)
		if element_exist :
			element_pointer.value = value

	def compute_nb_of_item(self) :
		counter = 0
		for i in self.list :
			counter += i.len()
		self.nb_of_item = counter
		return self.nb_of_item

	def compute_load_factor(self) :
		self.load_factor = self.compute_nb_of_item()/self.size
		return self.load_factor

if __name__ == '__main__' :

	dico = HashTable(10)
	for i in range(len(string.ascii_lowercase)) :
		dico.add_element((string.ascii_lowercase)[i], i)

	print(dico.does_exist("a"))
	dico.set_value("a", "ur mom is fat")
	print(dico.get_value("a"))


