#Mini script file which generates .c.gcov files, automatically, from source code and test examples.

import os
from file_work import find_files
from subprocess_helpers import run_gcc, run_tests, find_redundant

			
def main():
	print(os.getcwd())
	print("Insert file extension (c or cpp):")
	ext = input()
	print("Insert path without last /:")
	path = input()
	os.chdir(path)
	found = find_files(ext, '.')
	run_gcc(found)
	test_names = run_tests("test_info.run")
	find_redundant(test_names)
	
if __name__ == "__main__":
	main()