#Mini script file which generates .c.gcov files, automatically, from source code and test examples.
import os
from file_work import find_files
from run import run_gcc, run_tests, find_redundant
from min_cover import test_algorithms

			
def main():
	print("Insert file extension and path:")
	ext = input()
	print("Insert path without last /:")
	path = input()
	os.chdir(path)
	found = find_files(ext, '.')
	run_gcc(found)
	run_tests(path)
	#if run_gcc(found) == 1:
		#merge_gcovs()
	find_redundant()
	
if __name__ == "__main__":
	main()