import sys
import pytest
import sh
import subprocess


# subprocess.
def run_tests_advanced(config=None, reporting=None, tests=None):
    """Preparing list of tests for execution."""
    print "Running tests with specific parameters"
    # Remove previous tests directory and create new one
    sh.rm("-rf", './temp_tests')
    sh.mkdir('temp_tests')

    if tests != None:
        sh.cp('-r', './tests/base_test.py', './temp_tests')
        my_list = tests.split(",")
        for item in enumerate(my_list):
            sh.cp('-r', './tests/' + item[1], './temp_tests')
    else:
        sh.cp('-r', './tests/', './temp_tests')
    pytest.main('-v -x temp_tests')
    sh.rm('-rf', './temp_tests')
    print config
    print reporting


def generate_reports():
    pass


def read_config_file(filename=None):
    """Read configuration from provided config file."""
    vars = dict()
    with open(filename) as temp_file:
        for line in temp_file:
            eq_index = line.find('=')
            var_name = line[:eq_index].strip()
            number = line[eq_index + 1:].strip()
            vars[var_name] = number
    print str(vars)+"hehehe"
    print vars['browser']

def main():
    # print 'sys.argv[1]'+sys.argv[1]
    #print len(sys.argv)
    if len(sys.argv) > 1:
        arguments = sys.argv[1]
    else:
        arguments = None
    #read_config_file('atf.properties')
    #run_tests_advanced(tests=arguments)
    pytest.main('-v -x temp_tests')

if __name__ == '__main__':
    main()
