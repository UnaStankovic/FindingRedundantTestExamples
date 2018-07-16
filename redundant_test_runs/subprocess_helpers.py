from subprocess import check_output, CalledProcessError, Popen, PIPE
from file_work import coverage_array_creator, file_opener, find_files, write_array_to_file, read_array_from_file, delete_by_extension
from min_cover import min_set_coverage_optimal, min_set_coverage_greedy, min_set_coverage_redundant_pairs
import os
import numpy as np


def check_outputs(command, string):
	try:
		check_output(['bash', '-c', command])
		print(string)
	except CalledProcessError:
		print("CalledProcessError")
		exit()
		
def run_subprocess(command, string):
	try:
		p = Popen(command, shell=True, stdin=PIPE,stdout=PIPE,stderr=PIPE, universal_newlines=True)
		p.wait()
		print(string)
	except CalledProcessError:
		print("CalledProcessError")
		exit()
		
def run_subprocess_with_input(command, input):
	try:
		p = Popen(command, shell=False, stdin=PIPE,stdout=PIPE,stderr=PIPE, universal_newlines=True)	
		p.stdin.write(input)
		p.stdin.close()
		p.wait()
	except CalledProcessError:
		print("CalledProcessError")
		exit()
		
def run_gcov():
	found_files = find_files(".gcda", ".")
	for f in found_files:
		command = 'gcov ' + f
		run_subprocess(command,"Successfully generated .c.gcov.")
	return 1
	
def run_test(command, input):
	p = Popen(command, shell=False, stdin=PIPE,stdout=PIPE,stderr=PIPE, universal_newlines=True)
	p.stdin.write(input)
	p.stdin.close()
	#print(p.stdout.read())
	p.wait()
	
def run_tests(test_info_file):
	#test_info_file = os.path.join(path,"test_info.run")
	#test_info_file = "test_info.run"
	with open(test_info_file) as f:
		test_info = f.readlines()
	test_info = [x.rstrip() for x in test_info] 
	for test_name,test_command,test_input in zip(test_info[0::3], test_info[1::3], test_info[2::3]):
		delete_by_extension(os.curdir, ".gcda")
		#delete_by_extension(os.curdir, ".gcno")
		delete_by_extension(os.curdir, ".gcov")
		run_subprocess_with_input(test_command, test_input)
		run_gcov()
		merge_gcovs(test_name)

	delete_by_extension(os.curdir, ".gcda")
	delete_by_extension(os.curdir, ".gcov")
	delete_by_extension(os.curdir, ".gcno")
	test_names = test_info[0::3]
	return test_names

def run_gcc(found):
	command = 'gcc -g -Wall -fprofile-arcs -ftest-coverage -O0 -o test ' + ' '.join(found)	
	run_subprocess(command,"Successfully compiled with gcc.The test sample will be run now." )
	
def find_redundant(test_names):
	pathdata_files = find_files(".pathdata", ".")
	all_data = []
	for f in pathdata_files:
		array_data = np.array(read_array_from_file(f))
		all_data.append(array_data)
	all_data = np.array(all_data)
	
	#print(all_data)
	print("Greedy algorithm")
	res = min_set_coverage_greedy(all_data)
	print(res)
	print_redundant_names(res, test_names)
	#print(min_set_coverage_greedy(all_data))
	
	print("Pair-redundant algorithm")
	res = min_set_coverage_redundant_pairs(all_data)
	print(res)
	print_redundant_names(res, test_names)
	#print(min_set_coverage_redundant_pairs(all_data))
	
	print("Optimal algorithm")
	res = min_set_coverage_optimal(all_data)
	print(res)
	print_redundant_names(res, test_names)
	#print(min_set_coverage_optimal(all_data))
	
	delete_by_extension(os.curdir, ".pathdata")
	
def merge_gcovs(test_name):
	found_files = find_files(".gcov", ".")
	merged = []
	for f in found_files:
		opened = file_opener(f)
		merged.append(coverage_array_creator(opened))
	merged = [item for sublist in merged for item in sublist]
	print("Merged gcovs for one test:")
	#print(merged)
	
	merged_int = [ 1 if i!="#####" else 0 for i in merged]
	print(merged_int)
	prefix = "merged_gcov"
	extension = "pathdata"
	full_name = prefix+"."+test_name+"."+extension
	write_array_to_file(merged_int, full_name)
	
def print_redundant_names(redundant_array, test_names):
	print("Redundant tests:")
	for i in range(redundant_array.size):
		if (redundant_array[i]==0):
			print(test_names[i])
	