# FindingRedundantTestExamples
This project is a part of Master Studies' course of Software Verification. The main idea is to explore, experiment and try to develop a methodology of discovering and removing redundant test examples. This project is done in collaboration with Mirko Brkusanin and Milos Samardzija who also attend the course during summer semester of 2018.

In the .tex file there are sections which represent out train of thoughts. There we have presented various ideas, experiments done and tools used in a process. The whole text is written in Serbian. 

## using test_info.run.
	
    Requirements:
        - clang-format-6.0
        - python (compatible with python3)
        - numpy package

    Usage:
        - run python script with_test_info/redundant_tests.py
		- run example:
            cd with_test_info
            python3 redundant_tests.py
            c
            examples/01
			
    Available examples:
        examples/01
        examples/02
        examples/03
        examples/04

## using custom unit testing framework.

    Requirements:
        - clang-format-6.0
        - python (compatible with both python2.7 and python3)
        - numpy package

    Setup:
        - cd with_unit_test_framework
        - Run ./setup.sh (compiles custom unit testing framework)

    Usage:
        - Input
            python redundant_tests.py examples/01 
        - Output
            Redundant tests: 
            tst_03.test_deljenje2
			
        - Input (general usage)
            python redundant_tests.py {path to a test project} 
        - Output
            Redundant tests:
            {list of redundant tests}
            
    Available examples:
        - examples/01
        - examples/02
        - examples/03_false_positives
        - examples/04
        - examples/05_loop
