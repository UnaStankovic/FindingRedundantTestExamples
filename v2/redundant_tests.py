import sys
sys.path.insert(0,'../Tasks')

from helpers import *
from min_cover import min_set_coverage_optimal
import numpy as np

test_proj = load_test_project(sys.argv[1])
coverage_matrix = []
test_row = []

for test_case in test_proj['test_cases']:
	run_gcc(test_proj['libraries'] + [test_case['filename']])

	#get the name of the test case file, without extension
	test_case_name = get_filename(test_case['filename'])

	for test in test_case['tests']:
		#call current test only		
		call("./tst " + test)

		#remove .gcda for the test case source file
		os.remove(test_case_name + '.gcda')

		run_gcov()

		#calculate coverage array for the current test, and add it to the coverage matrix
		coverage_matrix.append(coverage_array_creator(list_dir('.', '.c.gcov')))
		test_row.append(test_case_name + '.' + test)

		#remove .gcda for the current test
		for file in list_dir('.', '.gcda'):
			os.remove(file)

#remove .gcno files
for file in list_dir('.', '.gcno'):
			os.remove(file)

#remove .c.gcov files
for file in list_dir('.', '.c.gcov'):
			os.remove(file)

#remove executable
os.remove('tst')

print('Redundant tests: ')
print(', '.join(np.array(test_row)[min_set_coverage_optimal(np.array(coverage_matrix)) == 0]))
