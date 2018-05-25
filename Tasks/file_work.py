def file_opener(filename):
	try:
		f = open(filename, 'r')
		return f
	except FileNotFoundError:
		print("The file does not exist.")
		exit()

def file_chooser():
	print("Insert filename:")
	name = input()
	if(name.find('.c.gcov') == -1):
		print("Not a valid option. Try again.")
		return file_chooser()
	else:
		return name
#ARRAY WORK		
def coverage_array_creator(f):
	coverage_array = []
	for line in f:
		line = line.lstrip()
		line = line.split(":")
		coverage_array.append(line[0])
	print("The coverage array is the following")
	print(coverage_array)
	return coverage_array