#Mini script file which generates .c.gcov files, automatically, from source code and test examples.
import os
from file_work import coverage_array_creator, file_opener, find_files, write_array_to_file
from run import run_gcc
from min_cover import test_algorithms

def merge_gcovs():
	found_files = find_files(".gcov", ".")
	merged = []
	for f in found_files:
		opened = file_opener(f)
		merged.append(coverage_array_creator(opened))
	merged = [item for sublist in merged for item in sublist]
	print("Merged gcovs for one test:")
	print(merged)
	
	merged_int = [ int(i) if i!="#####" else 0 for i in merged]
	print(merged_int)
	test_name = "0" # TODO: genereate name based on run test or test number
	prefix = "merged_gcov"
	extension = "pathdata"
	full_name = prefix+"."+test_name+"."+extension
	write_array_to_file(merged_int, full_name) #"merged_gcov.0.pathdata"
			
def main():

	print("Algorithm test")
	test_algorithms()
	print("Algorithm test -- end")


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