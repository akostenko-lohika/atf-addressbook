#!/bin/sh
# prepare keys
# example ./atf.sh <config file> <list of tests>
# <config file> is mandatory
# list of tests is not
# you can specify either test folders or specific test(s)
#

#cd /Users/andrijkostenko/PycharmProjects/atf-addressbook/src
#export PYTHONPATH=$PYTHONPATH:/Users/andrijkostenko/Documents/workspace/HelloWorld2/src
#export PYTHONPATH=$PYTHONPATH:/Users/andrijkostenko/PycharmProjects/atf-addressbook/src

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
# delete old tests if they exist
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

debug_level=`getTag debug_level ${PROPS_FILE}`
browser=`getTag browser ${PROPS_FILE}`
temp_location_for_tests=`getTag temp_location_for_tests ${PROPS_FILE}`
atfLocation=`getTag atfLocation ${PROPS_FILE}`

##Make sure we can find the atf.sh script (and that it's executable)
#if [ -x $ATFIMAGE/atf.sh ]; then
#    $ATFIMAGE/atf.sh $@
#    #Exit with the correct error code from the ATF
#    exit $?
#else
#    echo "The file $ATFIMAGE/atf.sh is not executable"
#    exit 1
#fi


echo $debug_level
echo $browser
echo $temp_location_for_tests
echo $ATFIMAGE
echo $atfLocation


if [ -z "$ATFIMAGE" ] || [ -z "$debug_level" ] || [ -z "$temp_location_for_tests" ] || [ -z "$atfLocation" ]
 then
    echo "Could not find all needed properties in the file ${PROPS_FILE}"
    exit 1
fi

rm -rf $ATFIMAGE/$temp_location_for_tests
mkdir $ATFIMAGE/$temp_location_for_tests
cp -r $ATFIMAGE/tests/* $ATFIMAGE/$temp_location_for_tests

#java -jar /Users/andrijkostenko/PycharmProjects/selenium-server-standalone-2.52.0.jar &
python core/ATFcore.py $temp_location_for_tests

#Make sure we can find the atf.sh script (and that it's executable)
#if [ -x $ATFIMAGE/atf.sh ]; then
#    $ATFIMAGE/atf.sh $@
#    #Exit with the correct error code from the ATF
#    exit $?
#else
#    echo "The file $ATFIMAGE/atf.sh is not executable"
#    exit 1
#fi
