import sys
import pytest


def main():
    # print 'sys.argv[1]'+sys.argv[1]
    #print len(sys.argv)
    parameters = None
    if len(sys.argv) > 1:
        arguments = sys.argv[1]
        parameters = sys.argv
    #python core/ATFcore.py temp_location results_dir PYTEST_PARAM browser test1 test2 test3...
    temp_test_location = parameters[1]
    results_dir = parameters[2]

    pytest.main(' --html='+results_dir+'/report.html --resultlog='+results_dir+'/results.log --junitxml '
                +results_dir+'/results.xml -v -x '+temp_test_location)
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
