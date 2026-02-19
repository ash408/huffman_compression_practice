
class Tree:
	def __init__(self, root):
		self.root = root


class Node:
	def __init__(self, character, frequency):
		self.character = character
		self.frequency = frequency
		self.binary = None

		self.left = None
		self.right = None


