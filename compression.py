#!/usr/bin/python3

import file_handling
from tree import Tree
from tree import Node

import base64


def main(location="test.b64"):
	encoded_data = retrieve_data(location)
	frequency_dict = find_frequency(encoded_data)
	nodes = frequency_to_nodes(frequency_dict)

	for node in nodes:
		print(node.character + ": " + str(node.frequency))

def retrieve_data(location):
	b64_data = file_handling.read_file_b64(location)
	encoded_data = base64.b64encode(b64_data).decode('utf-8')
	
	return encoded_data

def find_frequency(data):
	frequency_dict = {}

	for character in data:
		if character in frequency_dict:
			num = frequency_dict[character]
			frequency_dict[character] = num + 1
		
		else:
			frequency_dict[character] = 1

	return frequency_dict

def frequency_to_nodes(frequency_dict):
	nodes = []

	for character in sorted(frequency_dict, key=frequency_dict.get, reverse=True):
		frequency = frequency_dict[character]

		new_node = Node(character, frequency)
		nodes.append(new_node)

	return nodes


if __name__ == "__main__":
	main()
