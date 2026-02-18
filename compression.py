#!/usr/bin/python3

import file_handling
from data.tree import Tree
from data.tree import Node

import base64


def main(location="test.b64"):
	encoded_data = retrieve_data(location)
	frequency_dict = find_frequency(encoded_data)
	nodes = Tree.frequency_to_nodes(frequency_dict)

	for node in nodes:
		print(node.character + ": " + str(node.frequency))

def retrieve_data(location):
	b64_data = file_handling.read_file_b64(location)
	encoded_data = base64.b64encode(b64_data).decode('utf-8')
	
	return encoded_data


if __name__ == "__main__":
	main()
