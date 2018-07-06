# FindingRedundantTestExamples
This project is a part of my Master Studies' course of Software Verification. The main idea is to explore, experiment and try to develop a methodology of discovering and removing redundant test examples in big open source project such as llc tool for LLVM. This project is done in collaboration with Mirko Brkusanin and Milos Samardzija who also attend the course during summer semester of 2018th.

In the .tex file there are sections which represent out train of thoughts. There we have presented various ideas, experiments done and tools used in a process. The whole text is written in Serbian. 

LIBS:
- numpy (Python2.7)

V1.
1. run python script "Tasks/gen_gcov.py"
2. produce info about tests (such as extension and path)
   Example:
   $ python gen_gconv.py
   $ c
   $ ../Examples/01

V2.
1. Start Makefile (it compiles custom library for the tests that are given)
2. python redundant_tests.py path_to_test_project 
Output: list of redundant tests

python redundant_tests.py examples/01 