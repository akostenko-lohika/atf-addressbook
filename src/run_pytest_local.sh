#!/bin/sh
# prepare keys
# example ./atf.sh <config file> <list of tests>
# <config file> is mandatory
# list of tests is not
# you can specify either test folders or specific test(s)
#

#cd /Users/andrijkostenko/PycharmProjects/ATF/src/
#export PYTHONPATH=$PYTHONPATH:/Users/andrijkostenko/Documents/workspace/HelloWorld2/src
export PYTHONPATH=$PYTHONPATH:/Users/andrijkostenko/PycharmProjects/ATF/src

#python core/ATFcore.py -c 'run_tests()'
#python -c 'from core.ATFcore import *;run_tests_advanced(tests="'$1'");'
#RESULT_FOO=`python -c 'import test; print test.get_foo()'`
#ssh rakostenk@$1
#ssh admin@m1060s02.sma 'userconfig role new role1 description email ; commit "test"'

# python core/ATFcore.py config_file tests1 tests2
#python core/ATFcore.py $1 $2 $3

# analyze imput parameters,
# check if properties file exists
# read property file
# properties file should include:
# TEST_HOME = /home/user/testhome/
# PYTHON_VERSION
# BROWSER
# PYTHONPATH
# SELENIUM_OPTIONS
# RESULTS_DIR
# copy tests into TEST_HOME/tests/ directory
# then run python code


#cd TEST_HOME/tests
#and
#Create REPORT directory
#if it exists then rename it to REPORT_TIMESTAMP
# REPORT should include HTML,test reports and LOGS (atf.log)
# python atf_core.py PARAM1, PYTEST_PARAM2, REPORT...

#

# Use whitespece between shell script parameters

# read about virtual function

#iterate through all the arguments
for i in {1..10}
do
    py.test tests/test_olive3_local.py
done