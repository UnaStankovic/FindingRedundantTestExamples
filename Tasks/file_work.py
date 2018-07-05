import os 
import pickle

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

def find_files(ext, path):
	files_found = []
	for root, dirs, files in os.walk(path):
		for f in files:
			if f.endswith(ext) == True:
				files_found.append(root+ '/' +f)
	return files_found

def write_array_to_file(array, filename):	
	with open(filename, 'wb') as f:
		pickle.dump(array, f)
	
def read_array_from_file(filename):
	array = []
	with open(filename, 'rb') as f:
		array = pickle.load(f)
	return array

def delete_by_extension(dir_name, extension):
	dir = os.listdir(dir_name)

	for item in dir:
		if item.endswith(extension):
			os.remove(os.path.join(dir_name, item))

#ARRAY WORK		
def coverage_array_creator(f):
	coverage_array = []
	for line in f:
		line = line.lstrip()
		line = line.split(":")
		coverage_array.append(line[0])
	coverage_array = [x for x in coverage_array if x != '-']
	#print("The coverage array is the following")
	#print(coverage_array)
	return coverage_array