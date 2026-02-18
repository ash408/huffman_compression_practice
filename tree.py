
class Tree:
	def __init__(self, root):
		self.root = root

	def frequency_to_nodes(frequency_dict):
		nodes = []

		for character in sorted(frequency_dict, key=frequency_dict.get, reverse=True):
			frequency = frequency_dict[character]

			new_node = Node(character, frequency)
			nodes.append(new_node)

		return nodes


class Node:
	def __init__(self, character, frequency):
		self.character = character
		self.frequency = frequency

		self.left = None
		self.right = None


