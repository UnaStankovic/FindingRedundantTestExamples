#Mini script file which generates .c.gcov files, automatically, from source code and test examples.
import os 
from subprocess import check_output, CalledProcessError
from file_work import coverage_array_creator, file_opener

def find_files(ext, path):
	files_found = []
	for root, dirs, files in os.walk(path):
		for f in files:
			if f.endswith(ext) == True:
				files_found.append(root+ '/' +f)
	return files_found  
				
def check_input():
	print("Insert extension:")
	name = input()
	if(name == -1):
		print("Not a valid option. Try again.")
		return check_input()
	else:
		return name

def check_outputs(command, string):
	try:
		check_output(['bash', '-c', command])
		print(string)
	except CalledProcessError:
		print("CalledProcessError")
		exit()

def merge_gcovs():
	found_files = find_files(".gcov", ".")
	merged = []
	for f in found_files:
		opened = file_opener(f)
		merged.append(coverage_array_creator(opened))
	merged = [item for sublist in merged for item in sublist]
	print("Merged gcovs for one test:")
	print(merged)
	
def run_gcov():
	found_files = find_files(".gcda", ".")
	for f in found_files:
		command = 'gcov ' + f
		check_outputs(command,"Successfully generated .c.gcov.")
	merge_gcovs()
	
def run_test():
	command = './test'
	check_outputs(command, "Successfully runned test.")
	run_gcov()

def run_gcc(found):
	command = 'gcc -g -Wall -fprofile-arcs -ftest-coverage -O0 -o test ' + ' '.join(found)
	check_outputs(command,"Successfully compiled with gcc.The test sample will be runned now." )
	run_test()
			
def main():
	print("Insert file extension and path:")
	ext = input()
	print("Insert path without last /:")
	path = input()
	os.chdir(path)
	found = find_files(ext, '.')
	run_gcc(found)
	
if __name__ == "__main__":
	main()