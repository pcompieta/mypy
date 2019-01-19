import sys

def processLine(line):
    return processTokens(line.split())

def processTokens(tokens):
    mysum = sum( [int(s) for s in tokens if s.isdigit()] )
    return mysum

if __name__ == "__main__":
    for line in sys.stdin:
        print(processLine(line))
