#Mini script file which generates .c.gcov files, automatically, from source code and test examples.
import os 
from subprocess import check_output, CalledProcessError

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

def run_gcc(found):
	command = 'gcc -g -Wall -fprofile-arcs -ftest-coverage -O0 -o test ' + ' '.join(found)
	try:
		check_output(['bash', '-c', command])
		print("Successfully compiled with gcc.")
		return 
	except CalledProcessError:
		print("CalledProcessError")
		exit()
			
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