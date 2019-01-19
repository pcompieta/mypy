import sys

def sum_numbers(line):
    return sum( [int(s) for s in line.split() if s.isdigit()] )

if __name__ == "__main__":
    for line in sys.stdin:
        print(sum_numbers(line))
