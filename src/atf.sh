#!/bin/sh
# prepare keys
# example ./atf.sh <config file> <list of tests>
# <config file> is mandatory
# list of tests is not
# you can specify either test folders or specific test(s)
#

cd /Users/andrijkostenko/PycharmProjects/ATF/src/
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


#~/tests

#Function to read the value from a property out of a .properties file
getTag()
{
        grep "^$1=" $2 | awk -F= '{ print $2 }'
}

PROPS_FILE=
#iterate through all the arguments
for var in "$@"; do
    #find a valid file named "*.properties"
    if [[ $var == *.properties && -f $var ]]; then
        PROPS_FILE=$var
    fi
done
#Some error checking to make sure we could find the file
if [ -z "$PROPS_FILE" ]; then
    echo "Could not find the ATF .properties file in the supplied arguments [$@]"
    exit 1
fi
#Read the location if the ATF image
ATFIMAGE=`getTag atfLocation ${PROPS_FILE}`
if [ -z "$ATFIMAGE" ]; then
    echo "Could not find the property 'atfLocation' in the file ${PROPS_FILE}"
    exit 1
fi

echo browser
python core/ATFcore.py $2

#Make sure we can find the atf.sh script (and that it's executable)
#if [ -x $ATFIMAGE/atf.sh ]; then
#    $ATFIMAGE/atf.sh $@
#    #Exit with the correct error code from the ATF
#    exit $?
#else
#    echo "The file $ATFIMAGE/atf.sh is not executable"
#    exit 1
#fi
