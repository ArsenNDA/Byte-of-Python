import sys, warnings

if sys.version_info[0] < 3:
    warnings.warn("Python 3.6 or higher is recommended", RuntimeWarning)
else:
    print("Normal execution")
    print(">>>", sys.version_info)

