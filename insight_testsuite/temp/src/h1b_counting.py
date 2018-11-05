import sys

from CertificationPerformance import CertificationPerformance


if __name__ == '__main__':

    if len(sys.argv) != 4:
        sys.stderr.write("Usage: %s <input file path> <top occupation file path> <top states file path>" % (sys.argv[0],))

    CertificationPerformance(sys.argv[1:]).calculate_statistics()
