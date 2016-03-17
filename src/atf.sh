#!/bin/sh

# + analyze imput parameters,
# + check if properties file exists
# + read property file
# - properties file should include:
# TEST_HOME = /home/user/testhome/
# PYTHON_VERSION
# BROWSER
# PYTHONPATH
# SELENIUM_OPTIONS
# RESULTS_DIR

# + delete old tests if they exist
# + copy tests into temp directory
# + then run python code


# cd TEST_HOME/tests and
# + Create REPORT directory
# - if it exists then rename it to REPORT_TIMESTAMP
# - REPORT should include HTML,test reports and LOGS (atf.log)

# Use whitespece between shell script parameters






# Function to read the value from a property out of a .properties file
getTag()
{
        grep "^$1=" $2 | awk -F= '{ print $2 }'
}

PROPS_FILE=
# Iterate through all the arguments
for var in "$@"; do
    #find a valid file named "*.properties"
    if [[ $var == *.properties && -f $var ]]; then
        PROPS_FILE=$var
    fi
done

# Some error checking to make sure we could find the file
if [ -z "$PROPS_FILE" ]; then
    echo "Could not find the ATF .properties file in the supplied arguments [$@]"
    exit 1
fi

# Read the location if the ATF image
ATFIMAGE=`getTag ATFIMAGE ${PROPS_FILE}`
if [ -z "$ATFIMAGE" ]; then
    echo "Could not find the property 'ATFIMAGE' in the file ${PROPS_FILE}"
    #exit 1
fi

# Make current directory as ATFIMAGE if it was not specified in .properties file
if [ -z  $ATFIMAGE ]; then
    echo 'ATFIMAGE is empty, so make current directory as ATFIMAGE'
    ATFIMAGE=$(pwd)
fi

# Get list of parameters from .properties file
debug_level=`getTag debug_level ${PROPS_FILE}`
browser=`getTag browser ${PROPS_FILE}`
temp_location_for_tests=`getTag temp_location_for_tests ${PROPS_FILE}`
atfLocation=`getTag atfLocation ${PROPS_FILE}`
RESULTS_DIR=`getTag RESULTS_DIR ${PROPS_FILE}`

## Make sure we can find the atf.sh script (and that it's executable)
#if [ -x $ATFIMAGE/atf.sh ]; then
#    $ATFIMAGE/atf.sh $@
#    #Exit with the correct error code from the ATF
#    exit $?
#else
#    echo "The file $ATFIMAGE/atf.sh is not executable"
#    exit 1
#fi


#echo $debug_level
#echo $browser
#echo $temp_location_for_tests
#echo $ATFIMAGE
#echo $atfLocation

# Check whether all needed parameters are available
if [ -z "$ATFIMAGE" ] || [ -z "$debug_level" ] || [ -z "$temp_location_for_tests" ]
 then
    echo "Could not find all needed properties in the file ${PROPS_FILE}"
    exit 1
fi




# Delete old tests if they exist
rm -rf $ATFIMAGE/$temp_location_for_tests

# Create new temporary directory for tests
mkdir $ATFIMAGE/$temp_location_for_tests

# Start selenium server
#java -jar /Users/andrijkostenko/PycharmProjects/selenium-server-standalone-2.52.0.jar &

# Copy base_test to temporary directory
cp -r $ATFIMAGE/tests/base_test.py $ATFIMAGE/$temp_location_for_tests

# Get all passed tests and copy them to temporary directory
for var in "${@:2}"
do
    cp -r $ATFIMAGE/tests/$var $ATFIMAGE/$temp_location_for_tests
done

# + Create REPORT directory
# + if it exists then rename it to REPORT_TIMESTAMP
# - REPORT should include HTML,test reports and LOGS (atf.log)


if [ -d $ATFIMAGE/$RESULTS_DIR ]
then
    echo "Directory "$ATFIMAGE/$RESULTS_DIR" exists."
    mv $ATFIMAGE/$RESULTS_DIR $ATFIMAGE/$RESULTS_DIR-$(date +"%y-%m-%d-%H-%M")
else
    echo "Directory "$ATFIMAGE/$RESULTS_DIR" does not exist."
    mkdir $ATFIMAGE/$RESULTS_DIR
fi



# Run python code
# Example of python command: python core/ATFcore.py temp_location results_dir PYTEST_PARAM browser test1 test2 test3...
python core/ATFcore.py $temp_location_for_tests $RESULTS_DIR 'NoPytestParam' $browser

cp $RESULTS_DIR/results.xml $ATFIMAGE