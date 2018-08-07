inp = input("Type your mathematical sentence here:\n")

def tokenize(inp):
	chars = list(inp)
	clean_chars = []
	number = ""
	for i in chars:
		if i.isdigit():
			number += i
		elif i == "+" or i == "-":
			if number != "":
				clean_chars.append(number)
				clean_chars.append(i)
				number = ""
			else:
				clean_chars.append(i)
		elif not " ":
			raise ValueError("operation not supported")
		
	clean_chars.append(number)
	return clean_chars


def calculate(inp):
	cc = tokenize(inp)
	total = int(cc[0])
	op = ""
	for i in cc:
		if i == "+" or i == "-":
			op = i
		elif op == "+":
			total+=int(i)
			op = ""
		elif op == "-":
			total-=int(i)
			op = ""

	return total		

total = calculate(inp)
print(total)