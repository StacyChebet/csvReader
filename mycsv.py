import sys


def getdata():
    if len(sys.argv) == 1:  # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data.strip()


def readcsv(data):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """ 
    with open('AAPL.csv','r') as file:
        results = []
        for line in file:
            words = line.split(',')
            print(words)



    
    return header,data

if __name__ == '__main__':
  main()
