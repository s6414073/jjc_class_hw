#!/usr/bin/env python3

class ListNode:

	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:

	def __init__(self):
		self.head = None

	def add(self, data):
		new_node = ListNode(data)

		if self.head is None:
			self.head = new_node
		else:
			temp = self.head
			while temp.next is not None:
				temp = temp.next
			temp.next = new_node

	# position is 0 based
	def add_at(self, data, position):
		new_node = ListNode(data)

		if position < 0:
			print("Invalid position - " + str(position))
			return

		if position is 0:
			new_node.next = self.head
			self.head = new_node
			return

		temp = self.head
		count = 1
		while temp is not None and count < position:
			temp = temp.next
			count += 1

		if count is not position or temp is None:
			print("Invalid position - " + str(position))
		else:
			current_next = temp.next
			temp.next = new_node
			new_node.next = current_next

	def delete_last(self):
		temp = self.head

		if temp is None:
			print("Empty list")
			return

		prev = None
		while temp.next is not None:
			prev = temp
			temp = temp.next

		prev.next = None

	def print_list(self):
		temp = self.head

		while temp is not None:
			print(str(temp.data))
			temp = temp.next

if __name__ == '__main__':

	linked_list = LinkedList()
	
	linked_list.add(2)
	linked_list.add(4)
	linked_list.add(6)
	linked_list.add(1)
	
	
	linked_list.add_at(10, 1)
	linked_list.add_at(20, 3)
	linked_list.add_at(50, 0)
	linked_list.add_at(100, 3)
	linked_list.delete_last()
	linked_list.delete_last()
	linked_list.print_list()
