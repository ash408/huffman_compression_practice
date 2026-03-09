#!/usr/bin/python3

import file_handling
from data.tree_builder import TreeBuilder

import base64


def main(location="test.b64"):
	encoded_data = retrieve_data(location)
	codes = TreeBuilder(encoded_data).get_codes()
	file_handling.save_codes(codes)

	binary_data = compress_data(encoded_data, codes)
	file_handling.save_compressed(binary_data)

	new_binary = file_handling.read_compressed()
	loaded_codes = file_handling.read_json()

def retrieve_data(location):
	b64_data = file_handling.read_file_b64(location)
	encoded_data = base64.b64encode(b64_data).decode('utf-8')
	
	return encoded_data

def compress_data(encoded_data, codes):
	binary_data = ""

	for character in encoded_data:
		binary_data = binary_data + codes[character]

	print(binary_data)
	return int(binary_data, base=2)

def find_chunk(compressed_data, codes):
	compressed_data = str(compressed_data)
	b64_character = ""
	current_binary = ""

	for digit in compressed_data:
		current_binary = current_binary + digit

		for character, binary in codes.items():
			if current_binary == binary:
				b64_character = character

				return [b64_character, current_binary]


if __name__ == "__main__":
	main()
