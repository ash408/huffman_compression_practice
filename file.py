import base64


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

if __name__ == "__main__":
	main()
