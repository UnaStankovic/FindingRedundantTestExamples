#Mini script file which generates .c.gcov files, automatically, from source code and test examples.
import os
from file_work import coverage_array_creator, file_opener, find_files
from run import run_gcc

def merge_gcovs():
	found_files = find_files(".gcov", ".")
	merged = []
	for f in found_files:
		opened = file_opener(f)
		merged.append(coverage_array_creator(opened))
	merged = [item for sublist in merged for item in sublist]
	print("Merged gcovs for one test:")
	print(merged)
			
def main():
	print("Insert file extension and path:")
	ext = input()
	print("Insert path without last /:")
	path = input()
	os.chdir(path)
	found = find_files(ext, '.')
	if run_gcc(found) == 1:
		merge_gcovs()
	
if __name__ == "__main__":
	main()