#Parser for information extraction on executed lines. Output is an array of covered lines in source file 
from file_work import file_chooser, file_opener, coverage_array_creator

def compare_lines(first, second):
	array1 = coverage_array_creator(first)
	array2 = coverage_array_creator(second)
	counter = 0
	for i in range(len(array1)):
		if array1[i] == array2[i]:
			counter += 1
	if counter == len(array1):
		print("Test examples are equal - they cover the same branches.")
	else:
		print("Test examples cover different branches, so they are not equal.")
	return
		
def main():
	print("Input filenames for which you want to see if they have the same lines coverage:")
	f = file_chooser()
	s = file_chooser()
	first = file_opener(f)
	second = file_opener(s)
	
	compare_lines(first, second)

if __name__ == "__main__":
	main()