from subprocess import check_output, CalledProcessError
from file_work import find_files

def check_outputs(command, string):
	try:
		check_output(['bash', '-c', command])
		print(string)
	except CalledProcessError:
		print("CalledProcessError")
		exit()

def run_gcov():
	found_files = find_files(".gcda", ".")
	for f in found_files:
		command = 'gcov ' + f
		check_outputs(command,"Successfully generated .c.gcov.")
	return 1
	
def run_test():
	command = './test'
	check_outputs(command, "Successfully runned test.")
	return run_gcov()

def run_gcc(found):
	command = 'gcc -g -Wall -fprofile-arcs -ftest-coverage -O0 -o test ' + ' '.join(found)
	check_outputs(command,"Successfully compiled with gcc.The test sample will be runned now." )
	return run_test()
	