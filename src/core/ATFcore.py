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
    parameters = None
    if len(sys.argv) > 1:
        arguments = sys.argv[1]
        parameters = sys.argv
    else:
        arguments = None
    #read_config_file('atf.properties')
    #run_tests_advanced(tests=arguments)
    #python core/ATFcore.py temp_location results_dir PYTEST_PARAM browser test1 test2 test3...

    print 'parameters[0]:'+parameters[0]
    temp_test_location = parameters[1]
    print 'parameters[1]:'+parameters[1]
    results_dir = parameters[2]
    print 'parameters[2]:'+parameters[2]
    print 'parameters[3]:'+parameters[3]
    #print 'parameters[4]:'+parameters[4]
    #print 'parameters[5]:'+parameters[5]


    pytest.main(' --html='+results_dir+'/report.html --resultlog='+results_dir+'/results.log --junitxml '+results_dir+'/results.xml -v -x '+temp_test_location)
    # Usage if pytest:
    """
py.test --maxfail=2    # stop after two failures

py.test --showlocals # show local variables in tracebacks
py.test -l           # show local variables (shortcut)

py.test --tb=auto    # (default) 'long' tracebacks for the first and last
                     # entry, but 'short' style for the other entries
py.test --tb=long    # exhaustive, informative traceback formatting
py.test --tb=short   # shorter traceback format
py.test --tb=line    # only one line per failure
py.test --tb=native  # Python standard library formatting
py.test --tb=no      # no traceback at all

py.test --resultlog=path


    """

if __name__ == '__main__':
    main()
