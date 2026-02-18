
from data.tree import Tree
from data.tree import Node

class TreeBuilder:
	def __init__(self, data):
		self.root_nodes = []
		frequency_dict = TreeBuilder.find_frequency(data)
		self.node_heap = TreeBuilder.frequency_to_nodes(frequency_dict)

		self.tree = None
		

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

	#TODO
	def create_link(self):
    		pass
	#TODO
	def find_smallest_two(self):
		selected_nodes = []

		while len(selected_nodes) != 2:
			if len(self.root_nodes == 0):
				selected_nodes.append(self.node_heap.pop)
 
			else:
				selected_node = None
				heap_freq = self.node_heap[-1].frequency
 
				for current_node in self.root_nodes:
					if (current_node.frequency < heap_freq or
							selected_node is not None and
							current_node.frequency < selected_node.frequency):
						selected_node = current_node
 
				if selected_node is None:
					selected_nodes.append(node_heap.pop)
				else:
					selected_nodes.append(selected_node)
