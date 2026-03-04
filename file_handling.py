
import base64
import json


def main():
	b64_data = read_file_b64()
	print(b64_data)
	save_file_b64(b64_data)

def read_file_b64(location="test.txt"):
	b64_data = ""
	
	with open(location, 'rb') as file:
		bin_data = file.read()
		b64_data = base64.b64encode(bin_data)

	return b64_data

def save_file_b64(data, location="test.b64"):
	
	with open(location, 'wb') as file:
		file.write(data)

def save_codes(codes, location="test_codes.json"):

	with open(location, 'w+') as file:
		data = json.dumps(codes, indent=4)
		file.write(data)

def save_compressed(data, location="compressed_data.bin"):

	with open(location, 'wb') as file:
		file.write(data.to_bytes((data.bit_length()+7)//8, 'big'))

if __name__ == "__main__":
	main()
