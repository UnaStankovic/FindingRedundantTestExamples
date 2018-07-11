from subprocess import check_output, CalledProcessError
import os
import re

def list_dir(path, ext):
	files_found = []
	for root, dirs, files in os.walk(path):
		for f in files:
			if f.endswith(ext) == True:
				files_found.append(root + '/' + f)
	return files_found 

def get_filename(path_to_file, trim_ext = True):
	pos = path_to_file.rfind('/')

	if pos == -1:
		res = path_to_file
	else:
		res = path_to_file[pos + 1:]

	if trim_ext == True:
		return res[:res.rfind('.')]
	return res

def call(command):
	try:
		FNULL = open(os.devnull, 'w')
		result = check_output(['bash', '-c', command], stderr = FNULL)
		FNULL.close()

		return result
	except CalledProcessError as e:
		print("call {}".format(e))

def run_gcov():
	found_files = list_dir(".", ".gcda")
	for f in found_files:
		command = 'gcov ' + f
		call(command)

def run_gcc(source_files):
	framework_inc = 'test_framework/include/'
	framework_lib = 'test_framework/library/test.o'

	source_files.append(framework_lib)

	command = 'gcc -I ' + framework_inc + ' -g -fprofile-arcs -ftest-coverage -O0 -o tst ' + ' '.join(source_files)

	call(command)
	
#iterates over the list of gcda files, merges arrays of the parsed data, and returns that merged array
def coverage_array_creator(files):
	coverage_array = []
	for file in files:
		with open(file, 'r') as f:
			for line in f:
				line = line.lstrip()
				line = line.split(":")

				if line[0].isdigit():
					coverage_array.append(1)
				elif line[0].startswith('#'):
					coverage_array.append(0)
        print(coverage_array)
	return coverage_array

#returns a list of test cases and libraries used in the test project given as param test_path
def list_test_project(test_path):
	with open(test_path, 'r') as f:
		code = f.read()

	if re.search("#include \"test.h\"", code) != None:
		functions = []
		for m in re.finditer("ADD_TEST\((.*?)\)", code):
			functions.append(m.group(1))
		return {'filename' : test_path, 'tests' : functions}
	else:
		return {'filename' : test_path, 'tests' : None}

def reduce_function(acc, y):
	if y['tests'] != None:
		acc['test_cases'].append(y)
	else:
		acc['libraries'].append(y['filename'])
	return acc

#loads all relevant data about test project
def load_test_project(test_path):
	data = reduce(
		reduce_function,
		map(lambda f: list_test_project(f), list_dir(test_path, '.c')),
		{'test_cases' : [], 'libraries' : []}
	)

	return data
