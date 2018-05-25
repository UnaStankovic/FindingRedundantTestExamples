#Mini script file which generates .c.gcov files, automatically, from source code and test examples.
#Explanation: grab all .c .gcno and .gcda files to a common folder using find exec, then run gcov using the same command. 
# OTHER IDEA: find . -name "*.cpp" -exec sh -c 'gcov {} -o "$(dirname {})"' \;
LOCATION=../Examples/02/
FILENAME= find ${LOCATION} -name '*.c'
gcc -g -Wall -fprofile-arcs -ftest-coverage -O0 ../Examples/02/main.c -o test 
#find -name '*.c' -exec cp -t $LOCATION {} +
#find -name '*.gcno' -exec cp -t $LOCATION {} +
#find -name '*.gcda' -exec cp -t $LOCATION {} +
#cd $LOCATION
#find -name '*.c' -exec gcov -bf {} \;