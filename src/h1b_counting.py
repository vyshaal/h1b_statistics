import sys
import os

from CertificationPerformance import CertificationPerformance


if __name__ == '__main__':
    args = sys.argv

    if len(args) != 4:
        print("Incorrect arguments passed")
    elif not os.path.exists(args[1]):
        print("Input file not found")
    elif not (os.path.isdir(os.path.dirname(args[2])) and os.path.isdir(os.path.dirname(args[3]))):
        print("Output file directory doesn't exist")
    else:
        CertificationPerformance(args[1:]).calculate_statistics()
