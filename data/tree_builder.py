
from data.tree import Tree
from data.tree import Node

class TreeBuilder:
	def __init__(self, data):
		self.root_nodes = []
		frequency_dict = TreeBuilder.find_frequency(data)
		self.node_heap = TreeBuilder.frequency_to_nodes(frequency_dict)

		#self.tree = None
		self.create_link()
		print()
		self.create_link()

	#TODO finish required methods first
	def get_tree(self):
		#if self.tree is None:
		#	while len(self.node_heap) != 0:
		#		self.create_link()

		#return self.tree
		return None

	def frequency_to_nodes(frequency_dict):
		nodes = []

		for character in sorted(frequency_dict, key=frequency_dict.get, reverse=True):
			frequency = frequency_dict[character]

			new_node = Node(character, frequency)
			nodes.append(new_node)

		return nodes

	def find_frequency(data):
		frequency_dict = {}

		for character in data:
			if character in frequency_dict:
				num = frequency_dict[character]
				frequency_dict[character] = num + 1

			else:
				frequency_dict[character] = 1

		return frequency_dict

	#TODO remove this
	def view_node(self, node):
		print(str(node.character) + ": " + str(node.frequency))

		if node.left is not None:
			print("Left - " + str(node.left.character) + ": " + str(node.left.frequency))
		if node.right is not None:
			print("Right - " + str(node.right.character) + ": " + str(node.right.frequency))

	#TODO
	def create_link(self):
		nodes = self.find_smallest_two()
		node1, node2 = nodes[0], nodes[1]

		self.view_node(node1)
		self.view_node(node2)
		print()

		internal_node = Node(None, node1.frequency + node2.frequency)

		if node1.frequency < node2.frequency:
			internal_node.left = node1
			internal_node.right = node2
		else:
			internal_node.left = node2
			internal_node.right = node1

		self.view_node(internal_node)

		#self.view_node(internal_node)

		self.root_nodes.append(internal_node)
	
	#TODO test with root nodes
	def find_smallest_two(self):
		selected_nodes = []

		while len(selected_nodes) != 2:
			if len(self.root_nodes) == 0:
				selected_nodes.append(self.node_heap.pop())
 
			else:
				selected_node = None
				heap_freq = self.node_heap[-1].frequency

				remaining_roots = []
				for current_node in self.root_nodes:
					if (current_node.frequency < heap_freq):
						selected_node = current_node

					elif (selected_node is not None and
							current_node.frequency < selected_node.frequency):
						remaining_roots.append(selected_node)
						selected_node = current_node

					else:
						remaining_roots.append(current_node)

				self.root_nodes = remaining_roots				
 
				if selected_node is None:
					selected_nodes.append(self.node_heap.pop())
				else:
					selected_nodes.append(selected_node)
		return selected_nodes
